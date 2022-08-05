import RPi.GPIO as GPIO
from time import *
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


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

def int_to_bin_list(input_integer):
    # declaring variable for storing return output
    output_binary_list = [None]
    # using format() + list comprehension
    # decimal to binary number conversion 
    output_binary_list = [int(i) for i in list('{0:0b}'.format(input_integer))]
    # making the array of minimal expected length (adjusting to the number of LEDs to light: 5 for hours, 6 for minutes)
    while len(output_binary_list) < 6:
        output_binary_list = [0] + output_binary_list
    return output_binary_list



try:

    # list for single binary digits
    list_binary = [None]

    # list of GPIO pins to LEDs
    list_gpio = [26, 19, 13, 6, 5, 22]

    # initializing number 
    # int_input = 1
    int_input = int(input("Pass only an int value: "))

    # safety check for limited value of int_input: 24 for hours, 60 for minutes
    if int_input >60:
        GPIO.cleanup()
        print("Program ended due to int >60")
        quit()
    
    # printing original number
    print ("The original number is : " + str(int_input))
    
    # using int_to_bin_list function to transform int variable into list of binaries
    list_binary = int_to_bin_list(int_input)

    # printing the single items of the array
    for x in range(len(list_binary)):
        print(("Place ") + str(x) + ": " + str(list_binary[x]))

    # lighting up LEDs that correspond to positive binary positions
    binary_to_led(list_binary, list_gpio)

    # program shutdown
    sleep(3)
    GPIO.cleanup()
    print("Program ended")

except KeyboardInterrupt:
    print("Program stopped")
    GPIO.cleanup()
