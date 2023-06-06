def get_ints_from_user(user_in1 = None, user_in2 = None):
    if float(user_in1) and float(user_in2):
        if float(user_in2) > 0:
            rectangleA = float(user_in1) * float(user_in2)
            message = "Area of the rectangle: " + str(rectangleA)
        return message
        if float(user_in1) == float(user_in2):
            squareA = float(user_in1) * float(user_in2)
            message = "Area of the square: " + str(squareA)
        return message
    elif user_in1:
        squareA = float(user_in1) ** 2 
        message = "Area of the square: " + str(squareA)
        return message
    else:
        return "No input entered"
print("This program shows areas of a square or rectangle.")
user_in1 = input("Enter the length of the first side: ")
user_in2 = input("Enter the length of the first side: ")
print(get_ints_from_user(user_in1 or "", user_in2 or ""))