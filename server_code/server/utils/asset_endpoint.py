from anvil.server import (
    HttpResponse as _HttpResponse,
    http_endpoint as _http_endpoint,
)


class asset_endpoint:
    """Decorator for asset endpoint funcs"""

    def __init__(self, asset_type='html'):
        """."""
        self.asset_type = asset_type

    def __call__(self, func):
        """."""
        # Inspect func
        code_object = func.__code__
        pos_args_n = code_object.co_argcount
        # Get names of positional func parameters (incl. with default values)
        self.param_names = code_object.co_varnames[:pos_args_n]
        # Infer if func has a '**' parameter
        self.accept_query = func.__code__.co_flags & 0x08 != 0

        # Infer endpoint path from func name and its parameters
        self.path = f"/{func.__name__}".replace("_", "-")
        if self.param_names:
            self.path = self.path + '/:' + '/:'.join(self.param_names)
        if self.accept_query is True:
            self.url = self.url + '/'

        def response_func(*params, **q):
            """Returns HTTP response based on func return value. Called when endpooint invoked."""
            # Prepare HTTP response
            http_response = _HttpResponse()
            # Set headers based on asset type
            if self.asset_type == "css":
                http_response.headers = {"Content-Type": "text/css; charset=utf-8"}
            elif self.asset_type == "html":
                http_response.headers = {"Content-Type": "text/html; charset=utf-8"}
            elif self.asset_type == "jpg":
                http_response.headers = {"Content-Type": "image/jpeg"}
            elif self.asset_type == "js":
                http_response.headers = {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/javascript; charset=utf-8",
                }
            elif self.asset_type == "json":
                http_response.headers = {
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/json; charset=utf-8",
                }
            
            # Give func access to asset endpoint obj
            func._asset_endpoint = self

            # Set HTTP response body from func return value (the asset)
            http_response.body = func(*params, **q)

            return http_response

        # Register endpoint
        _http_endpoint(self.path, methods=["GET"])(response_func)
        # Make 'asset_endpoint' decorator stackable
        return func
