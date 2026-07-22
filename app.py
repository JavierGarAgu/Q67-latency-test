from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/plain"
        )

        self.end_headers()

        self.wfile.write(
            b"Registry performance test application"
        )


server = HTTPServer(
    ("0.0.0.0", 8080),
    Handler
)

print("Application running on port 8080")

server.serve_forever()
