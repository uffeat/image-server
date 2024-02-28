from anvil.server import (
    HttpResponse as _HttpResponse,
    http_endpoint as _http_endpoint,
    request as _request,
)




class asset_endpoint:
    """Decorator for asset endpoint funcs"""

    def __init__(
        self,
        type,
    ):
        """."""
        self._type = type


    def __call__(self, func):
        """."""

        def response_func_factory():
            """Returns a func that gets called when endpoint is invoked."""
            if self._type == 'css':
                response_headers = {
                    "Content-Type": "text/css; charset=utf-8"
                }
            elif self._type == 'html':
                response_headers = {
                    "Content-Type": "text/html; charset=utf-8"
                }
            elif self._type == 'jpg':
                response_headers = {
                    "Content-Type": "image/jpeg"
                }
            elif self._type == 'js':
                response_headers = {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/javascript; charset=utf-8"
                }
            elif self._type == 'json':
                response_headers = {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/json; charset=utf-8"
                }

            def response_func(*args, **kwargs):
                """"""
                http_response = _HttpResponse()
            
                asset = self._func(*args, **kwargs)
                http_response.body = asset

                http_response.headers = response_headers
        
                return http_response
            
            return response_func

        # Register endpoint
        name = f"/{func.__name__}".replace('_', '-')
        _http_endpoint(name, methods=["GET"])(response_func_factory)

        # Make 'asset_endpoint' decorator stackable
        return func

   
        

    
    
