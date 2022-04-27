import RPi.GPIO as GPIO
from time import *
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

try:
    while True:
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        sleep(1)
    
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        sleep(1)

except KeyboardInterrupt:
    print("Program stopped")
    GPIO.cleanup()