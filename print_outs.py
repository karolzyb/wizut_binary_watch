    
def welcome_print():
    """Function for printing welcome message"""
    print(f"Binary watch - default set to GMT/UTC timezone")
    print(f"Pass a single argument of integer number within scope -12 to 12 to set corresponding timezone")
    print(f"To stop press ctrl+c\n")

def time_test_print(arg_hour, arg_min, arg_sec):
    """Function to console-print current time. Takes three integers, respectively hours, minutes, seconds, as an argument."""
    # printing time in decimal format
    print(f"Decimal watch: {arg_hour:02d}:{arg_min:02d}:{arg_sec}")
    # printing time in binary format
    print(f"Binary watch: {arg_hour:05b}:{arg_min:06b}:{((arg_sec)%2):b}")

def print_warning():
    """Function to print a notice regarding possible command line arguments."""
    print(f"Run program again & Pass none or only one argument (int within -12 to 12)")