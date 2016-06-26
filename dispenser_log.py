import logging
import datetime
import os
import os.path

LOG_DIR = "log"
FILENAME_FORMAT = "%Y-%m-%d.log"

def setup_log():
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)
    log_filename = os.path.join(LOG_DIR, datetime.datetime.now().strftime(FILENAME_FORMAT))
    logging.basicConfig(filename=log_filename, level=logging.INFO)
    
