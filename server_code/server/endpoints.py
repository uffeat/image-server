from jinja2 import Template
import anvil.server
from anvil import URLMedia
from .db import get_image as _get_image


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
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "image/jpeg"
    }

    image = _get_image('test')

        
    response.body = image
    response.status = 200
        

    return response




@anvil.server.http_endpoint(
    "/get-page",
    methods=["GET"],
)
def get_page():
    response = anvil.server.HttpResponse()
    
    response.headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "text/html; charset=utf-8"
    }
 
    media = URLMedia('https://image-server.anvil.app/_/theme/index.html')
    media_bytes = media.get_bytes()
    raw_html = media_bytes.decode()

    template = Template(raw_html)

    # Render the template with context
    html = template.render(headline='Hello World')

    ##html = html.format(headline="Hello")

    response.body = html
    response.status = 200
    
    return response


@anvil.server.http_endpoint(
    "/my-url",
    methods=["GET"],
)
def get_page():
    response = anvil.server.HttpResponse()
    
    response.headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "text/plain; charset=utf-8"
    }
 
    
    response.status = 200
    
    return response