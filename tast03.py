
class Cage:
    def __init__(self):
        self.cell_cage = 12

    def __add__(self, cage):
        self.cell_cage = self.cell_cage * cage
        return self

    def __sub__(self, cage):
        if (self.cell_cage-(self.cell_cage * cage)) > 0:
            self.cell_cage -= (self.cell_cage * cage)
            return self
        else:
            print(f'Разность двух клеток должна быть больше 0')

    def __mul__(self, cage):
        self.cell_cage *= (self.cell_cage *cage)
        return self

    def __truediv__(self, cage):
        self.cell_cage = self.cell_cage/cage
        return self

    def __str__(self):
        return f'{self.cell_cage}'

    def make_order(self):
        n=0
        my_str = ''
        for i in range(self.cell_cage):
            n +=1
            if n==5:
                my_str += '*\\n'
#                my_str += '*\n'
                n=0
            else:
                my_str += '*'

        print(my_str)



cg = Cage()
cg * 3
print(cg)
cg.make_order()
