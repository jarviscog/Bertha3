from RaspberryPiCode.Bit import Bit
class BitArray:

    number_of_bits = 0
    width = 0
    height = 0

    def __init__(self, width:int, height:int):

        self.width = width
        self.height = height
        self.number_of_bits = width*height
        self.array = []
        for i in range(0,height):
            row = []
            for j in range(0,width):
                new_bit = Bit()
                row.append(new_bit)
            self.array.append(row)

    def set_bit(self, x,y, symbol):
        if (type(self.array[y][x]) == type(Bit())):
            self.array[y][x].flip_to(symbol)

    def display_string(self, input_string:str, starting_row:int = 0,ending_row:int = 0, overflow=False, whitespace_char=' ', align='L'):
        """

        :param input_string: The string to put on the screen
        :param starting_row: What row the text starts on
        :param ending_row: What row the text ends on
        :param overflow: What to do with overflow. This is currently unused
        :param whitespace_char: What to fill the empty space with
        :param align: To align on the left 'L', right 'R', or center 'C'
        :return:
        """
        # Clean some of the input
        align = align.upper()
        if align not in ['L','C','R']:
            print("Align value is not valid")
            return

        print("Setting String: " + input_string)
        string_width = len(input_string)

        # Control the input of Multi-line Strings

        if string_width > self.width:

            print("String too big to fit on one line. Recursivley splitting")
            input_string_array = input_string.split(" ")
            print(input_string_array)
            return

        # From here it is assumed the string is the right size and only one line, and no recursion will occur
        if(starting_row-ending_row==0):
            # It is assumed that the sting will be on one line
            if align == 'L':
                for i in range(0, len(self.array[0])):
                    print("Working on line")
                    if(i < len(input_string)):
                        character = input_string.upper()[i]
                        self.set_bit(i, starting_row, character)
                    else:
                        self.set_bit(i, starting_row, whitespace_char)
            elif align == 'C':
                print("Center")
                start_bit = len(self.array[0])/2 - len(input_string)/2
                end_bit = len(self.array[0])/2 + len(input_string)/2

                print(start_bit)
                print(end_bit)
                for i in range(0, len(self.array[0])):
                    print(i)



            if align == 'R':
                for i in range(0, len(self.array[0])):
                    print("Working on line")
                    string_starting_location = len(self.array[0]) - len(input_string) - 1
                    if(i > string_starting_location):
                        print(i)
                        print(string_starting_location)
                        index_location = i - string_starting_location - 1
                        print(index_location)
                        character = input_string.upper()[index_location]
                        self.set_bit(i, starting_row, character)
                    else:
                        self.set_bit(i, starting_row, whitespace_char)
        else:
            print("Error inserting: " + input_string)






    def print_letters(self):
        if self.array != None:
            print("|",end="")
            for i in range(0, len(self.array[0])):
                print("=====",end="")
            print("|")
            for row in self.array:
                for bit in row:
                    print("| %2s " % bit.symbol, end="")
                print(" |")

            print("|", end="")
            for i in range(0, len(self.array[0])):
                print("=====", end="")
            print("|")

    def print_locations(self):
        if self.array != None:
            print("|",end="")
            for i in range(0, len(self.array[0])):
                print("=====",end="")
            print("|")
            for row in self.array:
                for bit in row:
                    print("| %2s " % bit.location, end="")
                print(" |")

            print("|", end="")
            for i in range(0, len(self.array[0])):
                print("=====", end="")
            print("|")
