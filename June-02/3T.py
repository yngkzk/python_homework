def get_ints_from_user(user_in1 = None, user_in2 = None, user_in3 = None):
    if int(user_in1) and int(user_in2) and int(user_in3):
        operation = str(user_in1) + str(user_in2) + str(user_in3)
        final_num = int(operation)
        return final_num
    else:
        return "No input entered."
print("This program converts three different digits into one integer.")
user_in1 = input("Enter the first number: ")
user_in2 = input("Enter the second number: ")
user_in3 = input("Enter the third number: ")
print(get_ints_from_user(user_in1 or "", user_in2 or "", user_in3 or ""))