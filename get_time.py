import time

def get_time(input_arg_counter, input_arg_values):
        # pobieranie czasu
        if input_arg_counter == 2:
        #
            if int(input_arg_values[1]) >= -12 and int(input_arg_values[1]) <= 12:
                current_time = time.gmtime()
                return (current_time.tm_hour + (int(input_arg_values[1])))%24, current_time.tm_min, current_time.tm_sec
            else:
                print(f"Passed wrong argument")
        else:
            current_time = time.gmtime()
            return current_time.tm_hour, current_time.tm_min, current_time.tm_sec