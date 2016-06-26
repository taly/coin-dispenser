import time
import arm_controller

SLEEP_TIME = 0.2

arm_controller.setup()
arm_controller.on()

arm_controller.move_forward()
time.sleep(SLEEP_TIME)

arm_controller.move_back()
time.sleep(SLEEP_TIME)

#arm_controller.move_forward()
#time.sleep(SLEEP_TIME)

#arm_controller.move_back()
#time.sleep(SLEEP_TIME)

arm_controller.cleanup()
