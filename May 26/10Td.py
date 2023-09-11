mny = input("Enter your total monthly sales: ")
try:
    m = float(mny)
except ValueError:
    message = "Incorrect data"
else:
    x = 250
    y = m // 10
    result = 250 + y
    message = "Your wage is: $", result
print(message)