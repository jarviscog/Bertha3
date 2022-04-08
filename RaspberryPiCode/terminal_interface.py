from RaspberryPiCode.BitArray import BitArray

def main():

    print("Bertha3 Terminal Interface:")

    split_flap = BitArray(12,4)

    while True:
        split_flap.print_letters()
        in_string = input("Please enter a string: ")
        split_flap.display_string(in_string, align='C')

if __name__ == "__main__":
    main()