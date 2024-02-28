from anvil.server import (
    HttpResponse as _HttpResponse,
    http_endpoint as _http_endpoint,
)


class asset_endpoint:
    """Decorator for asset endpoint funcs"""

    def __init__(self, *params, type='html', accept_query=False):
        """."""
        self.params = params
        self.accept_query = accept_query
        self.type = type

    def __call__(self, func):
        """."""

        self.url = f"/{func.__name__}".replace("_", "-")
        if self.params:
            self.url = self.url + '/:' + '/:'.join(self.params)

        if self.accept_query is True:
            self.url = self.url + '/'

        def response_func_factory():
            """Returns a func that gets called when endpoint is invoked."""
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

            def response_func(*params, **q):
                """"""
                http_response = _HttpResponse()
                asset = self._func(*params, _meta=self, **q)
                http_response.body = asset

                http_response.headers = response_headers

                return http_response

            return response_func

        # Register endpoint
        
        

        _http_endpoint(self.url, methods=["GET"])(response_func_factory)

        # Make 'asset_endpoint' decorator stackable
        return func
