from random import randint


def make_matrix(n, m):
    a = []
    b = []
    for i in range(n):
        for x in range(m):
            b.append(randint(-10, 10))
        a.append(b)
        b = []

    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f'({a[i][j]})', end='  ')
        print()
    return a


def max_horizontal(matrix):
    max_numbers_info = ''
    for z in range(len(matrix)):
        max_number = None
        for y in range(len(matrix[z])):
            if max_number is None or matrix[z][y] > max_number:
                max_number = matrix[z][y]
        max_numbers_info += f'[{max_number}] - max number in [{z + 1}] horizontal line \n'
    print('')
    return max_numbers_info


def max_vertical(matrix):
    max_numbers_info = ''
    for u in range(len(matrix)):
        max_number = None
        for y in range(len(matrix[u])):
            if max_number is None or matrix[y][u] > max_number:
                max_number = matrix[y][u]
        max_numbers_info += f'[{max_number}] - max number in [{u + 1}] vertical line \n'
    print('')
    return max_numbers_info


def min_horizontal(matrix):
    min_numbers_info = ''
    for u in range(len(matrix)):
        min_number = None
        for y in range(len(matrix[u])):
            if min_number is None or matrix[u][y] < min_number:
                min_number = matrix[u][y]
        min_numbers_info += f'[{min_number}] - min number in [{y + 1}] horizontal line \n'
    print('')
    return min_numbers_info


def min_vertical(matrix):
    min_numbers_info = ''
    for u in range(len(matrix)):
        min_number = None
        for y in range(len(matrix[u])):
            if min_number is None or matrix[y][u] < min_number:
                min_number = matrix[y][u]
        min_numbers_info += f'[{min_number}] - min number in [{u + 1}] vertical line \n'
    print('')
    return min_numbers_info


my_matrix = make_matrix(3, 3)
print(max_horizontal(my_matrix))
print(max_vertical(my_matrix))
print(min_horizontal(my_matrix))
print(min_vertical(my_matrix))
