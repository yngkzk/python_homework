print("This program shows the number you entered is a leap year or not.")
user_in = input("Enter there the number: ")

try:
    user_in = int(user_in)
    year = user_in
except ValueError:
    msg = "Incorrect data, you have to enter a number!"
else:
    if year % 400 == 0:
        msg = str(year) + " is a leap year."
    elif year % 100 == 0:
        msg = str(year) + " is not a leap year."
    elif year % 4 == 0:
        msg = str(year) + " is a leap year."
    else:
        msg = str(year) + " is not a leap year."
print(msg)