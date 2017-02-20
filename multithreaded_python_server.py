#!/usr/bin/env python3
import sys
from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer

DEFAULT_PORT = 8000

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = DEFAULT_PORT

server = ThreadingSimpleServer(('', PORT), SimpleHTTPRequestHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
	print("Terminating server")