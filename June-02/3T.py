def combine_digits(user_in1, user_in2, user_in3):
    operation = str(user_in1) + str(user_in2) + str(user_in3)
    final_num = int(operation)
    return final_num
print("This program converts three different digits into one integer.")
user_in1 = input("Enter the first number: ")
user_in2 = input("Enter the second number: ")
user_in3 = input("Enter the third number: ")
print(combine_digits(user_in1, user_in2, user_in3))