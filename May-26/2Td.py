users_numb = input("Enter the first number: ")
users_numb2 = input("Enter the second number: ")
try:
    number = float(users_numb)
    number2 = float(users_numb2)
except ValueError:
    message = "incorrect data"
else:
    result = (number + number2) / 2
    message = "Your average number is: ", result
print(message)