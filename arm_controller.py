import time
import RPi.GPIO as GPIO

MOVE_TIME_SEC = 1
PAUSE_TIME_SEC = 1

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)

def on():
    GPIO.output(12, GPIO.HIGH)

def off():
    GPIO.output(12, GPIO.LOW)

def cleanup():
    GPIO.cleanup()

def move_forward():
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(8, GPIO.LOW)

def move_back():
    GPIO.output(10, GPIO.LOW)
    GPIO.output(8, GPIO.HIGH)
	
def dispense_coin():
    move_forward()
    time.sleep(PAUSE_TIME_SEC)
    move_back()

def get_total_dispensing_time():
    return MOVE_TIME_SEC * 2 + PAUSE_TIME_SEC    
    
