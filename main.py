import time
import datetime
import sched
import arm_controller
import dispenser_client

POLLING_INTERVAL = 1
PAUSE_BETWEEN_COINS_SEC = 2
DEBUG_FMT = "%H:%M:%S:%f"

def setup_arm():
    arm_controller.setup()
    arm_controller.on()
    #arm_controller.move_forward()
    arm_controller.move_back()
    time.sleep(arm_controller.MOVE_TIME_SEC)
    arm_controller.off()


def start_poll_loop():
    while True:
        debug("Polling...")
        to_dispense = dispenser_client.coins_to_dispense()
        debug("Got: %d" % to_dispense)
        while to_dispense > 0:
            debug("\tDispensing coin...")
            arm_controller.dispense_coin()
            sleep_time = arm_controller.get_total_dispensing_time()
            if to_dispense > 1:
                sleep_time += PAUSE_BETWEEN_COINS_SEC
            time.sleep(sleep_time)
            to_dispense -= 1
            debug("\t\tDispensed")
        time.sleep(POLLING_INTERVAL)


def debug(msg):
    print "%s: %s" % (datetime.datetime.now().strftime(DEBUG_FMT), msg)


if __name__ == "__main__":
    setup_arm()
    start_poll_loop()
        
            
        
        
