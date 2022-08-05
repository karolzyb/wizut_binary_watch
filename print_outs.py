    
def welcome_print():
    """Function for printing welcome message"""
    print(f"Binary watch - default set to GMT/UTC timezone")
    print(f"Pass a single argument of integer number within scope -12 to 12 to set corresponding timezone")
    print(f"To stop press ctrl+c\n")

def time_test_print(arg_hour, arg_min, arg_sec):
    # wyswietlanie w formie dziesietnej
    print(f"Decimal watch: {arg_hour:02d}:{arg_min:02d}:{arg_sec}")
    # wyswietlanie w formie binarnej
    print(f"Binary watch: {arg_hour:05b}:{arg_min:06b}:{((arg_sec)%2):b}")