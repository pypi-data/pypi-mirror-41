try:
    unicode('')
except NameError:
    # Python 3
    unicode = str

from cors.definitions import (CORS_RESPONSE_HEADERS, SIMPLE_METHODS, SIMPLE_REQUEST_CONTENT_TYPES,
                              SIMPLE_RESPONSE_HEADERS, get_prohibited_headers, is_same_origin,
                              is_simple_content_type, is_simple_method)
from cors.errors import AccessControlError, CORSError
from cors.utils import HeadersDict, Request


def format_header_field(header):
    return "-".join(map(str.capitalize, header.split("-")))


def check_origin(response, prepared_request):
    """
    Assert that a cross origin response allows requests from a request's origin.

    """
    request = prepared_request
    headers = HeadersDict(prepared_request.headers)
    if is_same_origin(request):
        return

    if "origin" not in headers:
        raise CORSError("Missing mandatory header 'Origin'")

    origin = headers["origin"]

    if response.headers.get("Access-Control-Allow-Origin") not in ("*", origin):
        raise AccessControlError(
            "Origin %r not allowed for resource %r" % (origin, request.url),
            request.url,
            request.method,
            request.headers)


def check_method(response, prepared_request):
    """
    Assert that the requested method is allowed.

    """
    request = prepared_request
    simple = request.method.upper() in SIMPLE_METHODS
    irregular_post = (
        request.method.upper() == "POST" and
        "Content-Type" in request.headers and
        request.headers["Content-Type"] not in SIMPLE_REQUEST_CONTENT_TYPES
    )

    if simple and not irregular_post:
        return

    allowed_methods = response.headers.get("Access-Control-Allow-Methods", "")
    allowed_methods = [
        allowed.strip().upper()
        for allowed in allowed_methods.split(",")
    ]

    if request.method.upper() not in allowed_methods:
        raise AccessControlError(
            "Method %r not allowed for resource %r" % (request.method, request.url),
            request.url,
            request.method,
            request.headers)


def check_headers(response, prepared_request):
    """
    Assert that the requested headers are allowed.

    """
    request = prepared_request
    allowed = response.headers.get("Access-Control-Allow-Headers", "")

    prohibited = get_prohibited_headers(request, allowed)
    if len(prohibited) == 0:
        return

    if prohibited == set(["content-type"]) and is_simple_content_type(request):
        return

    raise AccessControlError(
        "Headers %r not allowed for resource %r" % (prohibited, request.url),
        request.url,
        request.method,
        request.headers)


def prepare_preflight_allowed_origin(request):
    if is_same_origin(request):
        return {}, []
    return {}, [check_origin]


def prepare_preflight_allowed_methods(request):
    headers = {}
    checks = []
    if not is_simple_method(request):
        headers["Access-Control-Request-Method"] = request.method
        checks.append(check_method)

    content_type = request.headers.get("Content-Type", "text/plain")
    if content_type not in SIMPLE_REQUEST_CONTENT_TYPES:
        headers["Access-Control-Request-Headers"] = "Content-Type"
        checks.append(check_headers)

    return headers, checks


def prepare_preflight_allowed_headers(request):
    needed = get_prohibited_headers(request, {})
    needed = {format_header_field(h) for h in needed}

    if not is_simple_content_type(request):
        needed.add("Content-Type")

    if len(needed) == 0:
        return {}, []

    return (
        {"Access-Control-Request-Headers": ",".join(needed)},
        [check_headers]
    )


def prepare_preflight(request):
    """
    Generate a preflight request and followup checks.

    """
    headers = {}
    checks = []

    if request.method == "OPTIONS":
        return None, []

    for prep in (
            prepare_preflight_allowed_origin,
            prepare_preflight_allowed_headers,
            prepare_preflight_allowed_methods):
        required_headers, required_checks = prep(request)
        headers.update(required_headers)
        checks.extend(required_checks)

    # It is possible to have only one check (origin) which necessitates sending
    # a preflight request even though it won't include any CORS request headers.
    if len(headers) == 0 and len(checks) == 0:
        return None, []

    request_headers = HeadersDict(request.headers)
    headers["Host"] = request_headers.get("host", "")
    preflight = Request(
        "OPTIONS",
        request.url,
        headers)

    return preflight, checks


def generate_acceptable_preflight_response_headers(requested):
    """
    Given preflight request headers generate necessary CORS response headers.

    """
    response = {"Access-Control-Allow-Origin": "*"}

    if "Access-Control-Request-Method" in requested:
        method = requested["Access-Control-Request-Method"]
        response["Access-Control-Allow-Methods"] = method

    if "Access-Control-Request-Headers" in requested:
        headers = requested["Access-Control-Request-Headers"]
        response["Access-Control-Allow-Headers"] = headers

    return response


def generate_acceptable_actual_response_headers(response, origin=None):
    """
    Given the headers from an actual response add appropriate CORS response.

    """
    response = response.copy()
    if response.get("Access-Control-Allow-Origin", "") != origin:
        response["Access-Control-Allow-Origin"] = "*"

    exposed = response.get("Access-Control-Expose-Headers", "")
    exposed = exposed.split(",")
    exposed = map(lambda h: unicode(h).lower().strip(), exposed)
    received = response.keys()
    received = map(lambda h: unicode(h).lower().strip(), received)
    non_simple = set(received) - SIMPLE_RESPONSE_HEADERS - CORS_RESPONSE_HEADERS

    exposed = set(exposed) | non_simple
    exposed = [
        "-".join([p.capitalize() for p in h.split("_")])
        for h in exposed
    ]

    response["Access-Control-Expose-Headers"] = ",".join(exposed)
    return response
