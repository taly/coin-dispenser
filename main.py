import time
import datetime
import logging
import traceback
import arm_controller
import dispenser_client
import dispenser_log

POLLING_INTERVAL = 1
PAUSE_BETWEEN_COINS_SEC = 0.3
DEBUG_FMT = "%H:%M:%S:%f"

def setup_arm():
    logging.info("Setting up arm")
    arm_controller.setup()
    arm_controller.on()
    #arm_controller.move_forward()
    arm_controller.move_back()
    time.sleep(arm_controller.MOVE_TIME_SEC)
    arm_controller.off()


def start_poll_loop():

    logging.info("Starting polling loop")

    while True:
        time.sleep(POLLING_INTERVAL)
        try:
            poll()
        except Exception as e:
            logging.error("Exception during polling loop: %s" % traceback.format_exc())
            continue
    

def poll():
    
    logging.debug("Polling...")

    to_dispense = dispenser_client.coins_to_dispense()
    if to_dispense == dispenser_client.ERROR_VALUE:
        logging.error("Something went wrong with URL fetch, continuing loop")
        return

    log_str = "Got: %d" % to_dispense
    if to_dispense:
        logging.info(log_str)
    else:
        logging.debug(log_str)

    turn_off_arm = False
    if to_dispense > 0:
        arm_controller.on()
        turn_off_arm = True

    while to_dispense > 0:
        logging.info("\tDispensing coin...")
        arm_controller.dispense_coin()
        sleep_time = arm_controller.get_total_dispensing_time()
        if to_dispense > 1:
            sleep_time += PAUSE_BETWEEN_COINS_SEC
        time.sleep(sleep_time)
        to_dispense -= 1
        logging.info("\t\tDispensed")

    if turn_off_arm:
        arm_controller.off()


def debug(msg):
    print "%s: %s" % (datetime.datetime.now().strftime(DEBUG_FMT), msg)


if __name__ == "__main__":
    dispenser_log.setup_log()

    try:        
        setup_arm()
    except Exception as e:
        logging.error("Exception while setting up arm: %s" % traceback.format_exc())

    start_poll_loop()
        
            
        
        
