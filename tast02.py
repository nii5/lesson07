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
            return int(self.v / 6.5 + 0.5)
        else:
            return int(self.h * 2 + 0.3)


for i in range(5):
    textile = Clothes(my_dict[random.randint(1, 2)], random.randint(56, 64), random.randint(150, 196))
    print(f'{textile.my_type} {textile.expenditure}')
