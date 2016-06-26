import time
import datetime
import sched
import arm_controller
import dispenser_client

POLLING_INTERVAL = 5
PAUSE_BETWEEN_COINS_SEC = 2
DEBUG_FMT = "%H:%M:%S:%f"

working = False
coins_to_dispense = 0

def setup_arm():
    arm_controller.setup()
    arm_controller.on()
    #arm_controller.move_forward()
    arm_controller.move_back()
    time.sleep(arm_controller.MOVE_TIME_SEC)
    arm_controller.off()


def dispense_remaining_coins():
    global working
    global coins_to_dispense

    if working:
        return

    working = True
    while coins_to_dispense > 0:
        arm_controller.on()
        debug("Dispensing...")
        arm_controller.dispense_coin()
        coins_to_dispense -= 1
        sleep_time = arm_controller.get_total_dispensing_time()
        if coins_to_dispense > 1:
            sleep_time += PAUSE_BETWEEN_COINS_SEC
        time.sleep(sleep_time)
        debug("\tDispensed, coins left: %d" % coins_to_dispense)
    
    working = False
    arm_controller.off()


def poll(scheduler):
    global coins_to_dispense
    scheduler.enter(POLLING_INTERVAL, 1, poll, (scheduler,))    

    debug("Polling...")
    to_dispense = dispenser_client.coins_to_dispense()
    coins_to_dispense += to_dispense
    debug("\tPolled, got: %d, total: %d" % (to_dispense, coins_to_dispense))
    dispense_remaining_coins()


def start_poll_loop():
    print "Polling every %d secs..." % POLLING_INTERVAL

    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(1, 1, poll, (scheduler,))
    scheduler.run()


def debug(msg):
    print "%s: %s" % (datetime.datetime.now().strftime(DEBUG_FMT), msg)


if __name__ == "__main__":
    setup_arm()
    start_poll_loop()
        
            
        
        
