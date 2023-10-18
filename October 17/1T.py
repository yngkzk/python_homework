class Matrix:
    matrix = []
    current_row = -1
    rows = 0
    cols = 0

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        for x in range(rows):
            y = []
            self.matrix.append(y)
            for _ in range(cols):
                self.matrix[x].append(0)

    def __iter__(self):
        return self

    def __next__(self):
        if self.rows - 1 > self.current_row:
            self.current_row += 1
            return self.matrix[self.current_row]
        else:
            raise StopIteration

    def set(self, row, cells):
        for x in range(len(cells)):
            self.matrix[row][x] = cells[x]

    def show(self):
        print(self.matrix)

matrix = Matrix(3, 4)
matrix.show()

matrix.set(1, [1, 2, 3, 4])
matrix.show()

matrix.set(2, [5, 6, 7, 8])
matrix.show()

for x in matrix:
    print(x)
