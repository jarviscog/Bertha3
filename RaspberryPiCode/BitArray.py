from RaspberryPiCode.Bit import Bit
import textwrap
import math

class BitArray:
    """
    This is the object used to represent the display.
    """


    number_of_bits = 0
    width = 0
    height = 0

    def __init__(self, width:int, height:int):

        self.width = width
        self.height = height
        self.number_of_bits = width*height
        # self.array = [height][width]
        self.array = []
        for i in range(0,height):
            row = []
            for j in range(0,width):
                new_bit = Bit()
                row.append(new_bit)
            self.array.append(row)

    def set_bit(self, x,y, symbol):
        symbol = symbol.upper()
        if (type(self.array[y][x]) == type(Bit())):
            self.array[y][x].flip_to(symbol)

    def display_line(self, input_string, row = 0, align:chr = "L", whitespace_character = ' '):
        # TODO If the text would not fit on the display, this will crash
        # It is assumed that the sting will be on one line
        if align == 'L':
            for i in range(0, len(self.array[0])):
                # print("Working on line")
                if (i < len(input_string)):
                    character = input_string.upper()[i]
                    if character != " ":
                        self.set_bit(i, row, character)
                    else:
                        self.set_bit(i,row, whitespace_character)
                else:
                    self.set_bit(i, row, whitespace_character)
        elif align == 'C':

            # The floor here is so that if the string will not fit perfectly in the center, the string will be slightly to the left
            start_bit = math.floor(len(self.array[0]) / 2 - len(input_string) / 2)
            end_bit = start_bit + len(input_string)-1
            # print("Start bit: ", start_bit)
            # print("End bit: ", end_bit)
            for i in range(0, len(self.array[0])):
                # print("I: ", i)
                if i >= start_bit and i <= end_bit:
                    # print(i-start_bit)
                    character = input_string.upper()[i-start_bit]
                    self.set_bit(i, row, character)
                else:
                    self.set_bit(i,row, whitespace_character)
        if align == 'R':
            for i in range(0, len(self.array[0])):
                print("Working on line")
                string_starting_location = len(self.array[0]) - len(input_string) - 1
                if (i > string_starting_location):
                    print(i)
                    print(string_starting_location)
                    index_location = i - string_starting_location - 1
                    print(index_location)
                    character = input_string.upper()[index_location]
                    if character != " ":
                        self.set_bit(i, row, character)
                    else:
                        self.set_bit(i, row, whitespace_character)
                else:
                    self.set_bit(i, row, whitespace_character)

    def display_string(self, input_string:str, starting_row:int = 0,ending_row:int = 0, overflow=False, whitespace_char=' ', align='L'):
        """
        Takes a string as input and automatically fits it to the screen. There is a lot of UI options available in the form of arguments.
        If a string needs to be split over multiple rows in the display, each new substring will call self.display_line()
        :param input_string: The string to put on the screen
        :param starting_row: What row the text starts on
        :param ending_row: What row the text ends on
        :param overflow: What to do with overflow if the string is too long. This is currently unused
        :param whitespace_char: What to fill the empty space with
        :param align: To align on the left 'L', right 'R', or center 'C'
        :return:
        """
        # Clean some of the input
        align = align.upper()
        if align not in ['L','C','R']:
            print("Align value is not valid")
            return

        # print("Setting String: " + input_string)
        # This will take some word wrapping logic to work. Count the number of characters, divide by the number of
        # lines, then split the line based on where the spaces are
        number_of_characters = len(input_string)
        number_of_lines = ending_row-starting_row + 1
        optimal_char_count_per_line = number_of_characters/number_of_lines

        input_string_array = input_string.split(" ")

        difference_values = []
        for item in input_string_array:
            difference_values.append(len(item) - optimal_char_count_per_line)

        # print(number_of_characters)
        # print(number_of_lines)
        # print(optimal_char_count_per_line)
        # print(input_string_array)
        # print(difference_values)
        # Whoever made this package 🙏
        lines = textwrap.wrap(input_string, width=self.width)
        i = starting_row
        for line in lines:
            self.display_line(line,row=i, whitespace_character=whitespace_char,align=align)
            i+=1

        return

    def clear_screen(self, whitespace_char = ' '):
        """
        Sets the entire screen to the whitespace_char
        :param whitespace_char:
        :return:
        """
        for i in range(0,self.height):
            for j in range(0,self.width):
                self.set_bit(j,i,whitespace_char)

    def print_letters(self):
        """
        Prints a visualization of the split flap to the console
        :return:
        """
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
