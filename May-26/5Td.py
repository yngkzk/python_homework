users_numb = input("Enter the first number: ")
users_numb2 = input("Enter the second number: ")
try:
    n1 = float(users_numb)
    n2 = float(users_numb2)
except ValueError:
    message = "Incorrect data"
else:
    res1 = n1 + n2
    res2 = n1 - n2
    res3 = n1 * n2
    res4 = n1 / n2
    message = "The result of your action: ", "Addition: ", res1, "Subtraction: ", res2, "Multiplication: ", res3, "Division:", res4
print(message)