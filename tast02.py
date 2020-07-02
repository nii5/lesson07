import random

my_dict = {1: 'coat', 2: 'suit'}

class Clothes:
    def __init__(self, my_type, v, h):
        self.my_type = my_type
        self.v = v
        self.h = h

    @property
    def expenditure(self):
        if self.my_type == 'coat':
            return self.v / 6.5 + 0.5
        else:
            return self.v / 6.5 + 0.5

