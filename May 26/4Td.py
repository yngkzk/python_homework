number_req = input("Enter the number you want to convert to miles: ")
convertator = 0.621371
try:
    number = float(number_req)
except ValueError:
    message = "Incorrect data"
else:
    result = number * convertator
    message = "Your number in miles: ", result
print(message)