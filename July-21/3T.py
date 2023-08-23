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


def sum_vertical(matrix):
    summary = 0
    summary_list = []
    for z in range(len(matrix)):
        for y in range(len(matrix[z])):
            if matrix[y][z] % 2:
                summary += matrix[y][z]
        print(f'[{summary}]', end='  ')
        summary_list.append(summary)
        summary = 0
    print('vertical sum')
    return summary_list


def sum_horizontal(matrix):
    summary = 0
    summary_list = []
    for z in range(len(matrix)):
        for y in range(len(matrix[z])):
            if matrix[z][y] % 2:
                summary += matrix[z][y]
        print(f'[{summary}]', end='  ')
        summary_list.append(summary)
        summary = 0
    print('horizontal sum')
    return summary_list


my_matrix = make_matrix(3, 3)
# print(my_matrix)
vertical = sum_vertical(my_matrix)
# print(vertical)
horizontal = sum_horizontal(my_matrix)
# print(horizontal)
