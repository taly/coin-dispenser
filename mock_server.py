import json
from BaseHTTPServer import HTTPServer
from BaseHTTPServer  import BaseHTTPRequestHandler

to_dispense = 0

class JSONRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global to_dispense

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.wfile.write("\r\n")

        resp_json = {"coins": to_dispense}
        resp_str = json.dumps(resp_json)
        
        self.wfile.write(resp_str)
        to_dispense = 0

    def do_POST(self):
        global to_dispense

        to_dispense += 1
        print "POST: updating to %d" % to_dispense

print "Serving on localhost/8000..."

server = HTTPServer(("localhost", 8000), JSONRequestHandler)
server.serve_forever()
