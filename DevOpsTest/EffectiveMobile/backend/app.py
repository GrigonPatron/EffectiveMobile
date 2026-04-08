# app.py
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")

httpd = HTTPServer(("0.0.0.0", 8080), Handler)
print("Server started on 8080")
httpd.serve_forever()