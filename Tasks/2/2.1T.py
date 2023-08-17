# 2.1. Проверить истинность высказывания: "Квадратное уравнение Ax2 + Bx + C = 0
# с данными коэффициентами A, B, C имеет вещественные корни".

A = 2
B = 3
C = -14


for x in range(10):
    root = A * x ** 2 + B * x + C
    if root == 0:
        print('success!'
              '\nthe root is -', x)

# Not finished
