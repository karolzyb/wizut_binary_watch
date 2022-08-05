import sys

def safety_check(input_args):
    """Function for checking if passed arguments are valid (integer in range -12 to 12), takes system arguments as an input"""
    #sprawdzenie czy mamy 1 albo 0 argumentow do main
    if len(input_args) == 2:
        arg_string = input_args[1]
        # print(f"String: {arg_string}")

        #sprawdzenie czy mamy tylko inty (cyfry w zakresie 45-57 ASCII) i ewentualnie '-' (45 ASCII) dla liczb ujemnych
        for element in arg_string:
            # print(element)
            # print(ord(element))
            if (ord(element) < 45 or ord(element) > 57) and ord(element) != 45:
                print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
                sys.exit('Arg other than digits')

        #sprawdzenie czy mamy liczbe calkowita
        if float(arg_string)%1 != 0:
            # print(f"{float(arg_string)%1}")
            print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
            sys.exit('Not int number')

        #sprawdzenie zakresu -12 do 12
        if int(input_args[1]) >= -12 and int(input_args[1]) <= 12:
            print(f"Chosen timezone: {(int(input_args[1])):02d}:00 GMT")
            # print(f"{input_args[1][0]}")
        else:
            print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
            sys.exit('Int out of the scope')

    elif len(input_args) == 1:
        print(f"Chosen timezone: 00:00 GMT")

    else:
        print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
        # return(1)
        sys.exit('Too many args')