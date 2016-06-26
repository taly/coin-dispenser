import urllib2
import urllib
import httplib

HOST = "http://localhost"
PORT = 8000

def mock_dispense():
    print "Dispensing..."
    url = "%s:%d" % (HOST, PORT)
    data = urllib.urlencode({'dummy': 'dummy'})
    request = urllib2.Request(url, data)
    #request.add_header('Accept', '*/*')
    #request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1')
    try:
        urllib2.urlopen(request)    
    except httplib.BadStatusLine:
        pass
    

if __name__ == "__main__":
    while True:
        raw_input("\nPress ENTER to mock dispense")
        mock_dispense()
