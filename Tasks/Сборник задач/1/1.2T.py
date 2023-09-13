# 1.2. Даны два числа. Найти среднее арифметическое их квадратов и среднее арифметическое их модулей.

user_in1 = 1
user_in2 = -2.5

average_square = (user_in1 ** 2 + user_in2 ** 2) / 2
average_module = (((((user_in1 ** 2) ** 0.5) * 10) // 10) + ((((user_in2 ** 2) ** 0.5) * 10) // 10)) / 2

print('Average square -', average_square)
print('Average module -', average_module)
