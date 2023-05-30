print("This programm will show you the length of the side of the shape that you want")
user_in_diam = input("Enter the diameter of the circumscribed circle (cm):")
user_in_sides = input("Enter the quantity of the sides: ")
try:
    diam = float(user_in_diam)
    sides = int(user_in_sides)
except ValueError as err:
    message = ("Incorrect data", err)
else:
    degree = 3.14 / sides
    sin_angle = degree - degree ** 3 / 6 + degree ** 5 / 120 - degree ** 7 / 5040
    formula = diam * sin_angle
    form = ("Your length of the side is %.2f cm")
    message = form % formula
print(message)