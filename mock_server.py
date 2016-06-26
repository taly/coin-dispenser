from BaseHTTPServer import HTTPServer
from BaseHTTPServer  import BaseHTTPRequestHandler
import os.path

class JSONRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.wfile.write("\r\n")
        
        resp = "{\"coins\": 1}\n"
        self.wfile.write(resp)

print "Serving on localhost/8000..."

server = HTTPServer(("localhost", 8000), JSONRequestHandler)
server.serve_forever()
