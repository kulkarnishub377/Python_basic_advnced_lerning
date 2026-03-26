from wsgiref.simple_server import make_server
import urllib.parse
import json

class RouteInfo:
    def __init__(self, handler, methods):
        self.handler = handler
        self.methods = methods

class MiniFramework:
    def __init__(self):
        self.routes = {}

    def route(self, path, methods=None):
        """
        A decorator to register a function to a specific URL path.
        """
        if methods is None:
            methods = ['GET']
            
        def wrapper(handler):
            self.routes[path] = RouteInfo(handler, methods)
            return handler
        return wrapper

    def parse_query_string(self, environ):
        """Extracts ?key=value from the URL."""
        qs = environ.get('QUERY_STRING', '')
        return urllib.parse.parse_qs(qs)

    def __call__(self, environ, start_response):
        """
        This method makes instances of MiniFramework act as WSGI applications.
        It receives the environment dictionary and a start_response callable from the server.
        """
        path = environ.get('PATH_INFO', '/')
        method = environ.get('REQUEST_METHOD', 'GET')
        
        # Request context object to pass to the handler
        request = {
            'environ': environ,
            'method': method,
            'path': path,
            'query': self.parse_query_string(environ)
        }

        # 1. Route Matching
        if path in self.routes:
            route_info = self.routes[path]
            
            # 2. Method Checking
            if method not in route_info.methods:
                status = '405 Method Not Allowed'
                headers = [('Content-type', 'text/plain')]
                start_response(status, headers)
                return [b"405 Method Not Allowed"]
                
            # 3. Execution
            try:
                response_body, status_code, content_type = route_info.handler(request)
                
                status = f'{status_code} OK' if status_code == 200 else str(status_code)
                headers = [('Content-type', content_type)]
                start_response(status, headers)
                
                # WSGI expects an iterable of bytes
                if isinstance(response_body, str):
                    return [response_body.encode('utf-8')]
                elif isinstance(response_body, bytes):
                    return [response_body]
                else:
                    return [json.dumps(response_body).encode('utf-8')]
                    
            except Exception as e:
                status = '500 Internal Server Error'
                headers = [('Content-type', 'text/plain')]
                start_response(status, headers)
                return [f"500 Internal Error: {str(e)}".encode('utf-8')]
                
        else:
            # 404 Not Found
            status = '404 Not Found'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            return [b"404 Not Found"]

# ==========================================
# Example Usage of the MiniFramework
# ==========================================

app = MiniFramework()

@app.route('/', methods=['GET'])
def index(request):
    html = "<h1>Welcome to the Custom WSGI Framework!</h1><p>Try visiting <a href='/api/data'>/api/data</a> or <a href='/greet?name=Alice'>/greet?name=Alice</a></p>"
    return html, 200, 'text/html'

@app.route('/api/data', methods=['GET'])
def get_data(request):
    data = {"status": "success", "message": "JSON responses work natively."}
    return data, 200, 'application/json'

@app.route('/greet', methods=['GET'])
def get_greeting(request):
    # Safely extract query parameters
    name = request['query'].get('name', ['Guest'])[0]
    return f"Hello, {name}!", 200, 'text/plain'

if __name__ == '__main__':
    port = 8080
    with make_server('', port, app) as httpd:
        print(f"Serving on port {port}...")
        print("Press Ctrl+C to shut down.")
        httpd.serve_forever()
