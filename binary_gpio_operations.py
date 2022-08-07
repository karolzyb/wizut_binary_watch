import RPi.GPIO as GPIO

def int_to_bin_list(input_integer, max_len):
    """Function to convert integers into binary variables with adjusting the length of the output. 
    Takes integer value and integer of maximal length of binary variables list as an arguments.
    Returns list of binary values."""
    # declaring variable for storing return output
    output_binary_list = [None]
    # using format() + list comprehension
    # decimal to binary number conversion 
    output_binary_list = [int(i) for i in list('{0:0b}'.format(input_integer))]
    # making the array of minimal expected length (adjusting to the number of LEDs to light
    # max_len: 5 LEDs for hours, 6 LEDs for minutes, 1 LED for seconds)
    while len(output_binary_list) < max_len:
        output_binary_list = [0] + output_binary_list
    return output_binary_list

def binary_to_led(list_binaries, list_gpios):
    """Function to turn on LEDs connected to specified GPIOs. 
    Takes a list of GPIOs and list of binary values and combines both for lighting up only specified LEDs."""
    # iterate through the list of GPIOs to turn on/off the LEDs
    for i in range(len(list_gpios)):
        # looks for '0' binary values for LEDs being turned off
        if list_binaries[i] == 0:
            # print ("i: " + str(i) + " element z binary == 0")
            # print ("i: " + str(i) + " wartosc list_binary[i]: " + str(list_binary[i]))
            GPIO.output(list_gpios[i], GPIO.LOW)
        # others GPIOs binary values for LEDs being turned on
        else:
            # print ("i: " + str(i) + " element z binary == 1")
            # print ("i: " + str(i) + " wartosc list_binary[i]: " + str(list_binary[i]))
            GPIO.output(list_gpios[i], GPIO.HIGH)

def set_gpio_low(list_gpios):
    """Function to turn off LEDs connected to specified GPIOs. Takes a list of GPIOs to be turned off."""
    for i in range(len(list_gpios)):
        GPIO.output(list_gpios[i], GPIO.LOW)