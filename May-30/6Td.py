print("This program shows a discount that depends on the amount of your purchases.")
user_in = input("Enter there amount of your purchases: ")
try:
    amount = float(user_in)
except ValueError:
    msg = "Incorrect data."
except NameError as Nerr:
    msg = "Incorrect data: ", Nerr
if user_in == str(user_in):
    msg = "Incorrect data: " + user_in + ", You have to enter a number!"
elif 200 < amount < 300:
    discount = amount * 0.03
    result = amount - discount
    msg = "You have to pay: "
elif 300 < amount < 500:
    discount = amount * 0.05
    result = amount - discount
    msg = "You have to pay: "
elif 500 < amount:
    discount = amount * 0.07
    result = amount - discount
    msg = "You have to pay: "
elif amount < 200:
    msg = "There is no discount for you."
else: 
    msg = "Result."
print(msg, result, sep="")