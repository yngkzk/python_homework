users_req = input("Enter the length of the side of the square: ")
try:
    users_numb = float(users_req)
except ValueError:
    message = "Incorrect data"
else:
    result = users_numb ** 2
    message ="Your square area: ", result
print(message)