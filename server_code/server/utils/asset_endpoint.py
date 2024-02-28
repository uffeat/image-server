from anvil.server import (
    HttpResponse as _HttpResponse,
    http_endpoint as _http_endpoint,
)


class asset_endpoint:
    """Decorator for asset endpoint funcs"""

    def __init__(self, type='html'):
        """."""
        
        
        self.type = type

    def __call__(self, func):
        """."""
        code_object = func.__code__
        pos_args_n = code_object.co_argcount
        pos_arg_names = code_object.co_varnames[:pos_args_n]



        self.url = f"/{func.__name__}".replace("_", "-")
        if pos_arg_names:
            self.url = self.url + '/:' + '/:'.join(pos_arg_names)
        #if accept_query is True:
            #self.url = self.url + '/'

        def response_func(*params, **q):
            """."""
            if self.type == "css":
                response_headers = {"Content-Type": "text/css; charset=utf-8"}
            elif self.type == "html":
                response_headers = {"Content-Type": "text/html; charset=utf-8"}
            elif self.type == "jpg":
                response_headers = {"Content-Type": "image/jpeg"}
            elif self.type == "js":
                response_headers = {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/javascript; charset=utf-8",
                }
            elif self.type == "json":
                response_headers = {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/json; charset=utf-8",
                }

            
            http_response = _HttpResponse()
            func._asset_endpoint = self
            asset = func(*params, **q)
            http_response.body = asset

            http_response.headers = response_headers

            return http_response

            

        # Register endpoint
        
        

        _http_endpoint(self.url, methods=["GET"])(response_func)

        # Make 'asset_endpoint' decorator stackable
        return func
