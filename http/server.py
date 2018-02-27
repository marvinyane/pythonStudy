#! /usr/bin/python

import BaseHTTPServer
import time
import sys

HOST_NAME  = ''
PORT_NUMBER = 9090

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.send_header("Content-Length", 100)
        s.end_headers()

        s.wfile.write('This is a message ?\n')
        s.wfile.write('This is a message ?\n')
        s.wfile.write('This is a message ?\n')
        s.wfile.write('This is a message ?\n')
        s.wfile.write('This is a message ?\n')

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, int(sys.argv[1])), MyHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

