from RaspberryPiCode.BitArray import BitArray
from RaspberryPiCode.weather import get_weather
from RaspberryPiCode.spotify import sporify_handler
import time
from datetime import datetime
from RaspberryPiCode.constants import *

def main():

    print("Bertha3 Terminal Interface:")
    # num_of_rows = input("Enter the number of rows")
    # num_of_cols = input("Enter the number of columns")
    num_of_rows = 4
    num_of_cols = 14
    location = "Ilderton"
    whitespace_char = ' '

    split_flap = BitArray(num_of_cols,num_of_rows)

    while True:
        time.sleep(0.01)
        split_flap.print_letters()
        in_string = input("Please enter a selection. (h) for help: ").lower()
        # in_string = 'm'
        if in_string == 'h':
            print("(h)elp")
            print("(w)eather")
            print("(s)tring")
            print("(m)usic playing on spotify")
            print("(t)ime")
        elif in_string == 's':
            split_flap.clear_screen(whitespace_char)
            in_string = input("Please enter a string: ")
            split_flap.display_string(in_string, align='C', starting_row=1, ending_row=2, whitespace_char=whitespace_char)
        elif in_string == 'w':
            in_string = get_weather(location)
            split_flap.clear_screen(whitespace_char)
            split_flap.display_string(in_string, align='C', starting_row=0, ending_row=3, whitespace_char=whitespace_char)
        elif in_string == 'm':
            split_flap.clear_screen(whitespace_char)
            handler = sporify_handler(CLIENT_ID, CLIENT_SECRET)

            arr = handler.get_cleaned_song_info()
            arr.insert(1, "-")
            # pprint(arr)
            if arr:
                split_flap.display_layered_strings(arr, 0,4, align='C', whitespace_char=whitespace_char)
                # split_flap.display_string(arr[0], align='C', starting_row=0, ending_row=2, whitespace_char=' ')
                # split_flap.display_line(arr[1], align='C', row=3)
                # split_flap.display_line(arr[2], align='C', row=4)
        elif in_string == 't':

            split_flap.clear_screen()
            now = datetime.now()
            time_string = "Time: " + now.strftime("%H:%M:%S") + " in " + location
            split_flap.display_string(time_string, align='C')


if __name__ == "__main__":
    main()