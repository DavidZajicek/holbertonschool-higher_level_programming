#!/usr/bin/python3
"""
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class task_03_server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/':
            if self.path == '/status':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'OK')
            elif self.path == '/data':
                response = {"name": "John", "age": 30, "city": "New York"}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            elif self.path == '/info':
                response = {"version": "1.0",
                            "description": "A simple API built with http.server"}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                self.send_error(404, "Undefined Endpoint")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')


if __name__ == "__main__":
    httpd = HTTPServer(('', 8000), task_03_server)
    print('http://localhost:8000')
    httpd.serve_forever()
