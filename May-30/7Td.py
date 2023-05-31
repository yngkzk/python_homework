print("This proram shows can you fit a circle inside a square or not")
user_in_squ = input("Enter the periemeter of the square: ")
user_in_cir = input("Enter the circumference: ")

try:
    p = float(user_in_squ)
    C = float(user_in_cir)
    squareS = (p / 4) ** 2
    circleR = C / 2 * 3.14 
    circleS = 3.14 * circleR
except ValueError:
    msg = "Incorrect data. You have to enter numbers!"
except NameError as Nerr:
    msg = "Incorrect data.", Nerr
if squareS > circleS:
    msg = "You can fit a circle inside a square."
elif squareS < circleS:
    msg = "You can not fit a circle inside a square."
elif squareS == circleS:
    msg = "The area of the circle and the square is equal."
else:
    msg = "Result."
print(msg)