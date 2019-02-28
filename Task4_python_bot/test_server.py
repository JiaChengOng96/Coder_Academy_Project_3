#!/usr/bin/env python3
from http import HTTPStatus
import http.server
import socketserver
import os

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('content-length'))
        print('received: ' + str(self.rfile.read(content_length)))
        self.send_response(HTTPStatus.OK)
        self.end_headers()


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
