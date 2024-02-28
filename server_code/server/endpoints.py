from jinja2 import Template
import anvil.server
from anvil import URLMedia
from .db import get_image as _get_image
from anvil.server import get_app_origin

app_origin = get_app_origin()


@anvil.server.callable
def get_image(name):
    """."""
    return _get_image(name)

@anvil.server.http_endpoint(
    "/get-image",
    methods=["GET"],
)
def get_image():
    response = anvil.server.HttpResponse()
    
    response.headers = {
        ##"Access-Control-Allow-Origin": "*",
        "Content-Type": "image/jpeg"
    }

    image = _get_image('test')
    response.body = image
    ##response.status = 200
    return response

def get_asset(path: str) -> str:
    """."""
    media = URLMedia(f'https://image-server.anvil.app/_/theme/{path}')
    media_bytes = media.get_bytes()
    text = media_bytes.decode()
    return text





@anvil.server.http_endpoint(
    "/get-page",
    methods=["GET"],
)
def get_page():
    response = anvil.server.HttpResponse()
    
    response.headers = {
        ##"Access-Control-Allow-Origin": "*",
        "Content-Type": "text/html; charset=utf-8"
    }
 
    

    raw_html = get_asset('index.html')

    template = Template(raw_html)

    # Render the template with context
    html = template.render(headline='Hello World')

    ##html = html.format(headline="Hello")

    response.body = html
    ##response.status = 200
    
    return response


@anvil.server.http_endpoint(
    "/get-module",
    methods=["GET"],
)
def get_module():
    response = anvil.server.HttpResponse()
    
    response.headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/javascript; charset=utf-8"
    }
 
    media = URLMedia('https://image-server.anvil.app/_/theme/main.js')
    media_bytes = media.get_bytes()
    js = media_bytes.decode()

    
    response.body = js
    ##response.status = 200
    
    return response

@anvil.server.http_endpoint(
    "/get-styles",
    methods=["GET"],
)
def get_styles():
    response = anvil.server.HttpResponse()
    
    response.headers = {
        ##"Access-Control-Allow-Origin": "*",
        "Content-Type": "text/css; charset=utf-8"
    }
 
    media = URLMedia('https://image-server.anvil.app/_/theme/styles.css')
    media_bytes = media.get_bytes()
    css = media_bytes.decode()

    
    response.body = css
    ##response.status = 200
    
    return response