# ex4.2a.py Local web server


import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


handler = SimpleHTTPRequestHandler
server  = BaseHTTPServer.HTTPServer
protocol = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

address = ('127.0.0.1', port)

handler.protocol_version = protocol
httpd = server(address, handler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", address[0], "port", address[1], "..."
httpd.serve_forever()
