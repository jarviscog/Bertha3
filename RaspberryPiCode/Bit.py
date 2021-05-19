import MotorControl
class Bit:

    location = 0


    def __init__(self, pin1,pin2,pin3,pin4):

        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4

    def setRow(self, row):

        self.row = row

    def setColumn(self, column):

        self.column = column

    def setLocation(self, location):

        self.location = location

    def getLocation(self):

        return self.location

    def flip(self):

        MotorControl.tick(self.pin1, self.pin2, self.pin3, self.pin4)