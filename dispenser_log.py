import logging
import datetime
import os
import os.path

LOG_DIR = "/home/pi/coin-dispenser/log"
LOG_FORMAT = "%(asctime)s %(levelname)s %(module)s: %(message)s"
FILENAME_FORMAT = "%Y-%m-%d.log"

def basicConfig():
    log_filename = os.path.join(LOG_DIR, datetime.datetime.now().strftime(FILENAME_FORMAT))
    logging.basicConfig(filename=log_filename, format=LOG_FORMAT, level=logging.DEBUG)

def setup_log():
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)
    basicConfig()

def debug(msg):
    basicConfig()
    logging.debug(msg)

def info(msg):
    basicConfig()
    logging.info(msg)

def warning(msg):
    basicConfig()
    logging.info(msg)

def error(msg):
    basicConfig()
    logging.info(msg)
