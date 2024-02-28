from jinja2 import Template
import anvil.server
from anvil import URLMedia
from .db import get_image as _get_image
from anvil.server import HttpResponse, get_app_origin

app_origin = get_app_origin()

def create_response(content_type):
    """."""
    response = HttpResponse()
    if content_type == 'css':
        response.headers = {
            "Content-Type": "text/css; charset=utf-8"
        }
    elif content_type == 'html':
        response.headers = {
            "Content-Type": "text/html; charset=utf-8"
        }
    elif content_type == 'jpg':
        response.headers = {
            "Content-Type": "image/jpeg"
        }
    elif content_type == 'js':
        response.headers = {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/javascript; charset=utf-8"
        }
    elif content_type == 'json':
        response.headers = {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json; charset=utf-8"
        }
    return response

def get_asset(path: str) -> str:
    """."""
    media = URLMedia(f'{app_origin}/_/theme/{path}')
    media_bytes = media.get_bytes()
    text = media_bytes.decode()
    return text


@anvil.server.callable
def get_image(name):
    """."""
    return _get_image(name)


@anvil.server.http_endpoint(
    "/get-image",
    methods=["GET"],
)
def get_image(**q):

    print(q)
    response = create_response('jpg')
    image = _get_image('test')
    response.body = image
    return response



@anvil.server.http_endpoint(
    "/get-page",
    methods=["GET"],
)
def get_page():
    template = Template(get_asset('index.html'))
    response = create_response('html')
    response.body = template.render(headline='Hello World')
    return response


@anvil.server.http_endpoint(
    "/get-module",
    methods=["GET"],
)
def get_module():
    response = create_response('js')
    response.body = get_asset('main.js')
    return response

@anvil.server.http_endpoint(
    "/get-styles",
    methods=["GET"],
)
def get_styles():
    response = create_response('css')
    response.body = get_asset('styles.css')
    return response