import RPi.GPIO as GPIO

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

def set_gpio_low(input_list):
    for i in range(len(input_list)):
        GPIO.output(input_list[i], GPIO.LOW)