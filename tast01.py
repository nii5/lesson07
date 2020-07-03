
matrix_1 = [[31, 22], [37, 43], [51, 86]]
matrix_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
matrix_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]


class Matrix:

    def __init__(self):
        self.all_lists = []

    def __add__(self, other):
        for i in range(len(other)):
            try:
                self.all_lists[i]
            except:
                self.all_lists.append([])

            for j in range(len(other[0])):
                try:
                    self.all_lists[i][j] += other[i][j]
                except:
                    self.all_lists[i].append(0)
                    self.all_lists[i][j] += other[i][j]


        return self

    def __str__(self):
        return f'{self.all_lists}'


mx = Matrix()
mx + matrix_1 +matrix_2 + matrix_3
print(mx)
