print("Here is the formula for you: a * x + b = 0")
users_numb = input("Enter a value for 'a': ")
users_numb2 = input("Enter a value for 'b': ")
try:
    a, b = float(users_numb), float(users_numb2)
except ValueError:
    message = "Incorrect data"
else:
    given_formula = -b / a
    message = "Your 'X' is equals to: ", given_formula
print(message)