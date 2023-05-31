print("This program converts your number into a spec. symbol.")
un = input("Enter there your number from 0 to 9: ") # un - user's number
try:
    un = int(un)
except ValueError:
    msg = "Incorrect data, you have to enter a number from 0 to 9!"
except NameError:
    msg = "Incorrect data, you have to enter a number from 0 to 9!"

if un == str(un):
    msg = "Incorrect data: " + un + ", You have to enter a number from 0 to 9!"
elif un == 0:
    msg = "Here is your spec. symbol: ')'"
elif un == 1:
    msg = "Here is your spec. symbol: '!'"
elif un == 2:
    msg = "Here is your spec. symbol: '@'"
elif un == 3:
    msg = "Here is your spec. symbol: '#'"
elif un == 4:
    msg = "Here is your spec. symbol: '$'"
elif un == 5:
    msg = "Here is your spec. symbol: '%'"
elif un == 6:
    msg = "Here is your spec. symbol: '^'"
elif un == 7:
    msg = "Here is your spec. symbol: '&'"
elif un == 8:
    msg = "Here is your spec. symbol: '*'"
elif un == 9:
    msg = "Here is your spec. symbol: '('"
elif un < 0:
    msg = "Number cannot be negative! You have to enter a number from 0 to 9!"
elif un > 9:
    msg = "Your number is too high! You have to enter a number from 0 to 9!"
else:
    msg = "Result."

print(msg, sep=" ")