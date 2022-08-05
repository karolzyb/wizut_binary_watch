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

# lists for single binary digits of hours, minutes, seconds
list_h_binary = [None]
list_m_binary = [None]
list_s_binary = [None]

# lists of GPIO pins to LEDs reffering to hours, minutes, seconds
list_h_gpio = [20, 16, 12, 25, 24]
list_m_gpio = [26, 19, 13, 6, 5, 22]
list_s_gpio = [21]


def int_to_bin_list(input_integer, max_len):
    # declaring variable for storing return output
    output_binary_list = [None]
    # using format() + list comprehension
    # decimal to binary number conversion 
    output_binary_list = [int(i) for i in list('{0:0b}'.format(input_integer))]
    # making the array of minimal expected length (adjusting to the number of LEDs to light
    # max_len: 5 for hours, 6 for minutes, 1 for seconds)
    while len(output_binary_list) < max_len:
        output_binary_list = [0] + output_binary_list
    return output_binary_list

def binary_to_led(list_b, list_g):
    # iterate thru the list to turn on/off the LEDs
    for i in range(len(list_g)):
        if list_b[i] == 0:
            # print ("i: " + str(i) + " element z binary == 0")
            # print ("i: " + str(i) + " wartosc list_binary[i]: " + str(list_binary[i]))
            GPIO.output(list_g[i], GPIO.LOW)
        else:
            # print ("i: " + str(i) + " element z binary == 1")
            # print ("i: " + str(i) + " wartosc list_binary[i]: " + str(list_binary[i]))
            GPIO.output(list_g[i], GPIO.HIGH)


def main():
    print("Binary watch - default set to GMT/UTC timezone")
    print("Pass a single argument of integer number within scope -12 to 12 to set corresponding timezone")
    print("To stop press ctrl+c\n")

    #sprawdzenie czy mamy 1 albo 0 argumentow do main
    if len(sys.argv) == 2:
        string = sys.argv[1]
        # print(f"String: {string}")

        #sprawdzenie czy mamy tylko inty (cyfry w zakresie 45-57 ASCII) i ewentualnie '-' (45 ASCII) dla liczb ujemnych
        for element in string:
            # print(element)
            # print(ord(element))
            if ord(element) != 45 and (ord(element) < 45 or ord(element) > 57):
                print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
                sys.exit('Arg other than digits')

        #sprawdzenie czy mamy liczbe calkowita
        if float(string)%1 != 0:
            # print(f"{float(string)%1}")
            print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
            sys.exit('Not int number')

        #sprawdzenie zakresu -12 do 12
        if int(sys.argv[1]) >= -12 and int(sys.argv[1]) <= 12:
            print(f"Chosen timezone: {(int(sys.argv[1])):02d}:00 GMT")
            # print(f"{sys.argv[1][0]}")
        else:
            print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
            sys.exit('Int out of the scope')

    elif len(sys.argv) == 1:
        print(f"Chosen timezone: 00:00 GMT")

    else:
        print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
        # return(1)
        sys.exit('Too many args')

    while True:
        # pobieranie czasu
        if len(sys.argv) == 2:
        #
            if int(sys.argv[1]) >= -12 and int(sys.argv[1]) <= 12:
                current_time = time.gmtime()
                display_hour = (current_time.tm_hour + (int(sys.argv[1])))%24
                display_min = current_time.tm_min
                display_sec = current_time.tm_sec
            else:
                print(f"Passed wrong argument")
        else:
            current_time = time.gmtime()
            display_hour = current_time.tm_hour
            display_min = current_time.tm_min
            display_sec = current_time.tm_sec
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