import anvil.server
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

    

        
    response.body = '<h1>Hi</h1>'
    response.status = 200
        

    return response