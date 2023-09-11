fdn = input("Enter five digit number: ")
try:
    x = int(fdn)
except ValueError:
    message = "Incorrect data"
else:
    lastn = x % 10
    fourn = x // 10
    f = lastn * 10000
    t = fourn
    result = f + t
    message = "Your result is: ", result
print(message)