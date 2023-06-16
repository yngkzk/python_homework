print("This proram shows can you fit a circle inside a square or not")
user_in_squ = input("Enter the periemeter of the square: ")
user_in_cir = input("Enter the circumference: ")

try:
    user_in_squ = float(user_in_squ)
    user_in_cir = float(user_in_cir)
except ValueError:
    msg = "Incorrect data. You have to enter numbers!"
else:
    p = user_in_squ
    C = user_in_cir
    squareS = (p / 4) ** 2
    circleR = C / 2 * 3.14 
    circleS = 3.14 * circleR
    if squareS > circleS:
        msg = "You can fit a circle inside a square."
    elif squareS < circleS:
        msg = "You can not fit a circle inside a square."
    elif squareS == circleS:
        msg = "The area of the circle and the square are equal."
    else:
        msg = "Result."
print(msg)
