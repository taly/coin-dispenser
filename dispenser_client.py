import urllib2
import urllib
import json
import traceback
import dispenser_log

ERROR_VALUE = -1
#HOST = "http://localhost"
HOST = "https://coinme.herokuapp.com"
PORT = 8000

def coins_to_dispense():
    try:
        #url = "%s:%d" % (HOST, PORT)
        url = "%s/coins_to_dispense" % HOST
        raw_response = urllib2.urlopen(url)
        str_response = raw_response.read()
        json_response = json.loads(str_response)
        coins = json_response["coins"]
    except Exception as e:
        dispenser_log.error("Exception during fetching coins from server or formatting response: %s" % traceback.format_exc())
        return ERROR_VALUE

    return coins

def play_kaching():
    try:
        url = "https://cpc-curz-app.herokuapp.com/play"
        data = {"text": "coin"}
        data_post = urllib.urlencode(data)
        urllib2.urlopen(url=url, data=data_post)
    except Exception as e:
        dispenser_log.error("Coudln't play kaching: %s" % traceback.format_exc())
    
