tdn = input("Enter three digit number: ")
try:
    n = int(tdn)
except ValueError:
    message = "Incorrect data"
else:
    result = n % 100
    result2 = result // 10
    message = "The middle of the number equals: ", result2
print(message)