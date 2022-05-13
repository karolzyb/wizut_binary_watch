import RPi.GPIO as GPIO
from time import *
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)


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


try:

    # list for single binary digits
    list_binary = [None]

    # initializing number 
    # int_input = 1
    int_input = int(input("Pass only an int value: "))

    # safety check for limited value of int_input
    if int_input >24:
        GPIO.cleanup()
        print("Program ended due to int >24")
        quit()
    
    # printing original number
    print ("The original number is : " + str(int_input))
    
    # using format() + list comprehension
    # decimal to binary number conversion 
    list_binary = [int(i) for i in list('{0:0b}'.format(int_input))]

    # making the array of minimal expected length (adjusting to the number of LEDs to light: 5 for hours, 6 for minutes)
    while len(list_binary) < 5:
        list_binary = [0] + list_binary

    # printing the single items of the array
    for x in range(len(list_binary)):
        print(("Place ") + str(x) + ": " + str(list_binary[x]))

    # list of GPIO pins to LEDs
    list_gpio = [26, 19, 13, 6, 5]

    # lighting up LEDs that correspond to positive binary positions
    binary_to_led(list_binary, list_gpio)

    # program shutdown
    sleep(3)
    GPIO.cleanup()
    print("Program ended")

except KeyboardInterrupt:
    print("Program stopped")
    GPIO.cleanup()