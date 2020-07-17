from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(b'1337')

    def do_POST(self):
        self._set_headers()
        self.wfile.write(b'ok\n')

try:
    httpd = HTTPServer(('localhost', 8081), SimpleHTTPRequestHandler)
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Force close')