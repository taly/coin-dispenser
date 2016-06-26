import time
import arm_controller

arm_controller.setup()
arm_controller.on()

arm_controller.move_forward()
time.sleep(1)

arm_controller.move_back()
time.sleep(1)

arm_controller.move_forward()
time.sleep(1)

arm_controller.move_back()
time.sleep(1)

arm_controller.cleanup()
