import time
import sys

def main():
    print("Security for binary watch - default parameter = 0")
    print("Pass a single argument of integer number within scope -12 to 12")
    print("To stop press ctrl+c\n")

    #sprawdzenie czy mamy 1 albo 0 argumentow do main
    if len(sys.argv)==2:
        string = sys.argv[1]
        # print(f"String: {string}")

        #sprawdzenie czy mamy tylko inty (cyfry w zakresie 45-57 ASCII) i ewentualnie '-' (45 ASCII) dla liczb ujemnych
        for element in string:
            # print(element)
            # print(ord(element))
            if ord(element)!=45 and (ord(element)<45 or ord(element)>57):
                print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
                sys.exit('Arg other than digits')

        #sprawdzenie czy mamy liczbe calkowita
        if float(string)%1!=0:
            # print(f"{float(string)%1}")
            print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
            sys.exit('Not int number')

        #sprawdzenie zakresu -12 do 12
        if int(sys.argv[1])>=-12 and int(sys.argv[1])<=12:
            print(f"Chosen timezone: {(int(sys.argv[1])):02d}:00 GMT")
            # print(f"{sys.argv[1][0]}")
        else:
            print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
            sys.exit('Int out of the scope')

    elif len(sys.argv)==1:
        print(f"Chosen timezone: 00:00 GMT")

    else:
        print(f"Run program again & Pass none or only one argument (int within -12 to 12)")
        # return(1)
        sys.exit('Too many args')

    # while True:
    #     # pobieranie czasu
    #     if len(sys.argv)==2:
    #     #
    #         if int(sys.argv[1])>=-12 and int(sys.argv[1])<=12:
    #             current_time = time.gmtime()
    #             display_hour = (current_time.tm_hour + (int(sys.argv[1])))%24
    #             display_min = current_time.tm_min
    #             display_sec = current_time.tm_sec
    #         else:
    #             print(f"Passed wrong argument")
    #     else:
    #         current_time = time.gmtime()
    #         display_hour = current_time.tm_hour
    #         display_min = current_time.tm_min
    #         display_sec = current_time.tm_sec
    #     # wyswietlanie w formie dziesietnej
    #     print(f"Decimal watch: {display_hour:02d}:{display_min:02d}:{display_sec}")
    #     # wyswietlanie w formie binarnej
    #     print(f"Binary watch: {display_hour:05b}:{display_min:06b}:{((display_sec)%2):b}")
    #     time.sleep(1)

    print(f"Program runs correctly")

try:
    main()

except KeyboardInterrupt:
    print("Program stopped")