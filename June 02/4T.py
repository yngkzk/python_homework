def get_area(user_in1, user_in2=None):
    if user_in2 and int(user_in2) > 0:
        rectangleA = float(user_in1) * float(user_in2)
        message = "Area of the rectangle: " + str(rectangleA)
        return message
    elif user_in1:
        squareA = float(user_in1) ** 2
        message = "Area of the square: " + str(squareA)
        return message
    else:
        return "No input entered"
print("This program shows areas of a square or rectangle.")
user_in1 = input("Enter the length of the first side: ")
user_in2 = input("Enter the length of the second side (if rectangle, otherwise press enter): ")
print(get_area(user_in1, user_in2))