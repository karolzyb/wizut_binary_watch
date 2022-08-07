import sys
from print_outs import *


def safety_check(input_args):
    """Function for checking if passed argument is valid (integer in range -12 to 12). Takes command line arguments as an input"""
    # check for number of passed command line arguments
    if len(input_args) == 2:
        arg_string = input_args[1]
        # print(f"String: {arg_string}")

        # check for having only integers (digits withing range of 45-57 ASCII codes) and possibly for '-' sign (45 ASCII code) for negative numbers
        for element in arg_string:
            # print(element)
            # print(ord(element))
            if (ord(element) < 45 or ord(element) > 57) and ord(element) != 45:
                print_warning()
                sys.exit('Arg other than digits')

        # check for having only integer number
        if float(arg_string)%1 != 0:
            # print(f"{float(arg_string)%1}")
            print_warning()
            sys.exit('Not int number')

        # check for input being in range within -12 to 12
        if int(input_args[1]) >= -12 and int(input_args[1]) <= 12:
            # confirmation of correct command line argument
            print(f"Chosen timezone: {(int(input_args[1])):02d}:00 GMT")
            # print(f"{input_args[1][0]}")
        else:
            print_warning()
            sys.exit('Int out of the scope')

    # processing with one valid command line argument 
    elif len(input_args) == 1:
        print(f"Chosen timezone: 00:00 GMT")

    # condition met when passed more than one command line argument
    else:
        print_warning()
        sys.exit('Too many args')