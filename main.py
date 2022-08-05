#----------------------------------------------------------------------------
# Created By  : Karol Zyber
# Created Date: 2022-08-05
# version ='1.0'
# ---------------------------------------------------------------------------
# Binary watch - python3 script
# Wydzial Informatyki ZUT
# Studia podyplomowe z zakresu programowania z elementami systemow wbudowanych
# ---------------------------------------------------------------------------

import RPi.GPIO as GPIO
import time
import sys
from binary_operations import *
from get_time import *
from safety_check import *
from welcome_print import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# lists of GPIO pins to LEDs reffering to hours, minutes, seconds
list_h_gpio = [20, 16, 12, 25, 24]
list_m_gpio = [26, 19, 13, 6, 5, 22]
list_s_gpio = [21]

# lists for single binary digits of hours, minutes, seconds
list_h_binary = [None]
list_m_binary = [None]
list_s_binary = [None]


def main():

    welcome_print()

    safety_check(len(sys.argv), sys.argv)

    while True:

        display_hour, display_min, display_sec = get_time(len(sys.argv), sys.argv)

        # # wyswietlanie w formie dziesietnej
        # print(f"Decimal watch: {display_hour:02d}:{display_min:02d}:{display_sec}")
        # # wyswietlanie w formie binarnej
        # print(f"Binary watch: {display_hour:05b}:{display_min:06b}:{((display_sec)%2):b}")

        list_h_binary = int_to_bin_list(display_hour, 5)
        list_m_binary = int_to_bin_list(display_min, 6)
        list_s_binary = int_to_bin_list(display_sec%2, 1)
        binary_to_led(list_h_binary, list_h_gpio)
        binary_to_led(list_m_binary, list_m_gpio)
        binary_to_led(list_s_binary, list_s_gpio)

        time.sleep(0.2)


try:
    main()

except KeyboardInterrupt:
    print("Program stopped")
    # setting all gpios as LOW
    for i in range(len(list_h_gpio)):
        GPIO.output(list_h_gpio[i], GPIO.LOW)
    for i in range(len(list_m_gpio)):
        GPIO.output(list_m_gpio[i], GPIO.LOW)
    for i in range(len(list_s_gpio)):
        GPIO.output(list_s_gpio[i], GPIO.LOW)
    # cleanup for setting gpios as input (default)
    GPIO.cleanup()