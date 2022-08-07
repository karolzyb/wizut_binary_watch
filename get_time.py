import time

def get_time(input_args):
    """Function for parsing GMT time into separated variables of hours, minutes and seconds. 
    Takes system arguments as an input to adjust chosen timezone.
    Returns three int variables """
    # condition with parameter passed during startup of the program - int value for adjusting the timezone
    if len(input_args) == 2:
        if int(input_args[1]) >= -12 and int(input_args[1]) <= 12:
            current_time = time.gmtime()
            return (current_time.tm_hour + (int(input_args[1])))%24, current_time.tm_min, current_time.tm_sec
    # condition for GMT/UTC timezone (00:00)
    else:
        current_time = time.gmtime()
        return current_time.tm_hour, current_time.tm_min, current_time.tm_sec