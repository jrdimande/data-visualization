from random import randint

class Die():
    def __init__(self, num_sides=8):
        self.num_Sides = num_sides

    def roll(self):
        return randint(1, self.num_Sides)
