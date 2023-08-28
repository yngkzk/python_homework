number_req = input("Enter the number: ")
try:
    number = float(number_req)
except ValueError:
    message = "Incorrect data"
else:
    result = number ** 2
    message = "Your number squared is: ", result
print(message)