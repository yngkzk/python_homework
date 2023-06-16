def compare_numbers(user_in1, user_in2):
    if user_in1 and user_in2:
        if user_in1 == 0 and user_in2 == 0:
            message = 0
        if user_in1 > user_in2:
            message = 1
        if user_in1 < user_in2:
            message = -1
        if user_in1 == user_in2:
            message = 0
        return int(message)
    else:
        return "No input entered."
print("This program shows which number is greater and are they equal or not. (1 = first number is greater) (-1 = second number is greater) (0 = numbers are equal)")
user_in1 = input("Enter the first number: ")
user_in2 = input("Enter the second number: ")
print(compare_numbers(user_in1, user_in2))