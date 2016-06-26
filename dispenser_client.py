import urllib2
import json
import logging
import traceback

ERROR_VALUE = -1
#HOST = "http://localhost"
HOST = "https://coinme.herokuapp.com"
PORT = 8000

def coins_to_dispense():
#    url = "%s:%d" % (HOST, PORT)
    try:
        url = "%s/coins_to_dispense" % HOST
        raw_response = urllib2.urlopen(url)
        str_response = raw_response.read()
        json_response = json.loads(str_response)
        coins = json_response["coins"]
    except Exception as e:
        logging.error("Exception during fetching coins from server or formatting response: %s" % traceback.format_exc())
        return ERROR_VALUE

    return coins
