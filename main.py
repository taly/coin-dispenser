import time
import arm_controller
import dispenser_client

def setup_arm():
    arm_controller.setup()
    arm_controller.on()
    #arm_controller.move_forward()
    arm_controller.move_back()
    time.sleep(1)
    arm_controller.cleanup()

if __name__ == "__main__":
#    setup_arm()
    dispenser_client.coins_to_dispense()
