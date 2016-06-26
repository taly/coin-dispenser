import urllib2
import json

HOST = "http://localhost"
PORT = 8000

def coins_to_dispense():
    url = "%s:%d" % (HOST, PORT)
    raw_response = urllib2.urlopen(url)
    str_response = raw_response.read()
    json_response = json.loads(str_response)
    return json_response["coins"]
