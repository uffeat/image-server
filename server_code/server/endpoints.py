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
    html = media_bytes.decode()

    html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="shortcut icon" href="#" type="image/x-icon" />
    <title>Index</title>
    <link rel="stylesheet" href="/_/theme/styles.css">
    
    <script type="module" src="/_/theme/main.js"></script>
  </head>
  <body>
    <h1>{headline}</h1>
  </body>
</html>
"""

    html.format(headline="Hello")



    response.body = html



    response.status = 200
        

    return response