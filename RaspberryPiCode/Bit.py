import time

class Bit:

    number_of_positions = 0

    location = 0
    symbol = " "

    def __init__(self):

        self.flap_symbols = []

        self.flap_symbols.append(' ')
        for i in range(ord('A'), ord('Z') + 1):
            self.flap_symbols.append(chr(i))
        for i in range(0,10):
            self.flap_symbols.append(str(i))
        self.flap_symbols.append('#')
        self.flap_symbols.append('*')
        self.flap_symbols.append('-')
        self.flap_symbols.append('.')
        self.flap_symbols.append(':')

        self.number_of_positions = len(self.flap_symbols)

    def _setLocation(self, location):

        self.location = location

    def getLocation(self):

        return self.location

    def flip(self):
        # time.sleep(0.5)
        self.location +=1;
        if(self.location==self.number_of_positions):
            self.location = 0
            self.symbol = self.flap_symbols[0]
        self.symbol = self.flap_symbols[self.location]

    def flip_to(self, desired_symbol):
        flipping = True
        if desired_symbol in self.flap_symbols:
            while flipping:
                self.flip()
                if self.symbol == desired_symbol:
                    flipping = False
        else:
            print("Symbol [" + desired_symbol + "] is not in the split flap. Flipping to first symbol")
            # I don't know why, but making this recursive makes me nervous. The only way this can get out of control
            # is if self.flap_symbols is changing, which it shouldn't unless something has gone terribly wrong anyways.
            self.flip_to(self.flap_symbols[0])



    def __str__(self):
        return self.symbol
    def __int__(self):
        return self.location