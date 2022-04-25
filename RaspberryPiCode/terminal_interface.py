from RaspberryPiCode.BitArray import BitArray
from RaspberryPiCode.weather import get_weather

def main():

    print("Bertha3 Terminal Interface:")
    # num_of_rows = input("Enter the number of rows")
    # num_of_cols = input("Enter the number of columns")
    num_of_rows = 4
    num_of_cols = 12

    split_flap = BitArray(num_of_cols,num_of_rows)

    while True:
        split_flap.print_letters()
        in_string = input("Please enter a selection. (h) for help: ").lower()
        if in_string == 'h':
            print("(h)elp")
            print("(w)eather")
            print("(s)tring")
        elif in_string == 's':
            in_string = input("Please enter a string: ")
            split_flap.display_string(in_string, align='C', starting_row=1, ending_row=2, whitespace_char=' ')
        elif in_string == 'w':
            in_string = get_weather()
            split_flap.display_string(in_string, align='C', starting_row=1, ending_row=2, whitespace_char=' ')

if __name__ == "__main__":
    main()