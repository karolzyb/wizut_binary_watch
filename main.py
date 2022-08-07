#----------------------------------------------------------------------------
# Created By  : Karol Zyber
# Created Date: 2022-08-07
# version ='1.0'
# ---------------------------------------------------------------------------
# Binary watch - python3 script
# Wydzial Informatyki ZUT
# Studia podyplomowe z zakresu programowania z elementami systemow wbudowanych
# ---------------------------------------------------------------------------

import RPi.GPIO as GPIO
import time
import sys
from binary_gpio_operations import *
from get_time import *
from print_outs import *
from safety_check import *

# initial GPIO setup
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
    safety_check(sys.argv)

    while True:
        current_hour, current_min, current_sec = get_time(sys.argv)
        # time_test_print(current_hour, current_min, current_sec)
        list_h_binary = int_to_bin_list(current_hour, 5)
        list_m_binary = int_to_bin_list(current_min, 6)
        list_s_binary = int_to_bin_list(current_sec%2, 1)
        binary_to_led(list_h_binary, list_h_gpio)
        binary_to_led(list_m_binary, list_m_gpio)
        binary_to_led(list_s_binary, list_s_gpio)

        time.sleep(1)


try:
    main()

except KeyboardInterrupt:
    print(f" Program stopped")
    # setting all gpios as LOW
    set_gpio_low(list_h_gpio)
    set_gpio_low(list_m_gpio)
    set_gpio_low(list_s_gpio)

    # cleanup for setting gpios as input (default)
    GPIO.cleanup()