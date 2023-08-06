import re

from past.builtins import basestring

from .errors import CORSError

try:
    # python 3
    import urllib.parse as urlparse
    from urllib.parse import urljoin, urlparse as parse
except ImportError:
    # python 2
    import urlparse
    from urlparse import urljoin, urlparse as parse  # noqa: F401


CORS_REQUEST_HEADERS = set([
    "access-control-request-method",
    "access-control-request-headers",
])

CORS_RESPONSE_HEADERS = set([
    "access-control-allow-origin",
    "access-control-allow-methods",
    "access-control-allow-headers",
    "access-control-allow-credentials",
    "access-control-expose-headers",
    "access-control-max-age",
])

SIMPLE_METHODS = set([
    "GET",
    "HEAD",
    "POST",
])

# Headers which will be included in a request but not set by the application.
SIMPLE_AGENT_HEADERS = set([
    "accept-encoding",
    "connection",
    "content-length",
    "host",
    "origin",
])

SIMPLE_AUTHOR_HEADERS = set([
    "accept",
    "accept-language",
    "content-language",
])

SIMPLE_RESPONSE_HEADERS = set([
    "cache-control",
    "content-language",
    "content-type",
    "expires",
    "last-modified",
    "pragma",
])

SIMPLE_REQUEST_CONTENT_TYPES = set([
    "application/x-www-form-urlencoded",
    "multipart/form-data",
    "text/plain",
])


def _normalize_list(list_):
    if isinstance(list_, basestring):
        list_ = [v.strip() for v in list_.split(",")]
    return [v.lower() for v in list_]


def _normalize_origin_url(origin):
    origin_parts = urlparse.urlparse(origin)
    origin = [origin_parts.scheme, "://", origin_parts.netloc]
    if not re.search(r":\d+$", origin_parts.netloc):
        origin.append(":443" if origin_parts.scheme == "https" else ":80")
    return "".join(origin)


def is_same_origin(request):
    """
    Whether or not the request origin matches the host.

    """
    headers = dict([(k.lower(), v) for k, v in request.headers.items()])
    host = _normalize_origin_url(request.url)
    if "origin" not in headers:
        raise CORSError("Missing mandatory header 'Origin'")

    origin = _normalize_origin_url(headers["origin"])
    return host == origin


def is_simple_method(request):
    return (
        request.method.upper() in SIMPLE_METHODS and
        is_simple_content_type(request)
    )


def is_simple_content_type(request):
    return (
        "content-type" not in request.headers or
        request.headers["content-type"] in SIMPLE_REQUEST_CONTENT_TYPES
    )


def get_prohibited_headers(request, allowed):
    requested = set(map(str.lower, request.headers.keys()))
    implicit = (SIMPLE_AUTHOR_HEADERS | SIMPLE_AGENT_HEADERS | CORS_REQUEST_HEADERS)
    allowed = set(_normalize_list(allowed))
    return requested - implicit - allowed
