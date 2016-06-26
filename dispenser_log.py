import logging
import datetime
import os
import os.path

LOG_DIR = "/home/pi/coin-dispenser/log"
LOG_FORMAT = "%(asctime)s %(levelname)s %(module)s: %(message)s"
FILENAME_FORMAT = "%Y-%m-%d.log"

def setup_log():
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)
    log_filename = os.path.join(LOG_DIR, datetime.datetime.now().strftime(FILENAME_FORMAT))
    logging.basicConfig(filename=log_filename, format=LOG_FORMAT, level=logging.INFO)
    
