def get_ints_from_user(user_in1, user_in2):
    if float(user_in1) and float(user_in2):
        if user_in1 > user_in2:
            message = "1"
        if user_in1 < user_in2:
            message = "-1"
        if user_in1 == user_in2:
            message = "0"
        return message
    else:
        return "No input entered."
print("This program shows which number is greater and are they equal or not. (1 = first number is greater) (-1 = second number is greater) (0 = numbers are equal)")
user_in1 = input("Enter the first number: ")
user_in2 = input("Enter the second number: ")
print(get_ints_from_user(user_in1 or "", user_in2 or ""))
