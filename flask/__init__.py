class Flask:
    def __init__(self, name):
        self.routes = {}
        self.name = name

    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '/')
        if path in self.routes:
            response = self.routes[path]()
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
            if isinstance(response, str):
                response = response.encode('utf-8')
            return [response]
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
        return [b'404 Not Found']

    def run(self, host='127.0.0.1', port=5000, debug=False):
        from wsgiref.simple_server import make_server
        with make_server(host, port, self) as httpd:
            print(f'Serving on http://{host}:{port} ...')
            httpd.serve_forever()

def render_template_string(template_str, **context):
    return template_str
