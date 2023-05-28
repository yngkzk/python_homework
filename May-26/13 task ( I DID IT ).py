print("This programm will show you the length of the side of the shape that you want")
user_in_diam = input("Enter the diameter of the circumscribed circle: ")
user_in_sides = input("Enter the quantity of the sides: ")
try:
    diam = int(user_in_diam)
    sides = int(user_in_sides)
except ValueError as err:
    message = ("Incorrect data", err)
else:
    formula = diam * (3.14 / sides)
    form = ("Your length of the side is %.2f")
    message = form % formula
print(message)

'''VN: Очень хорошая попытка, но пока что в формуле есть ошибка:
Enter the diameter of the circumscribed circle: 10
Enter the quantity of the sides: 3
Your length of the side is 10.47

Длина стороны вписанного треугольника получилась больше, чем диаметр окружности.
С нетерпением жду ваше исправленное решение :)
'''