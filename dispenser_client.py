import urllib2

HOST = "http://localhost"
PORT = 8000

def coins_to_dispense():
    url = "%s:%d" % (HOST, PORT)
    resp = urllib2.urlopen(url)
    print resp.read()
