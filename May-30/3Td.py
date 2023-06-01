print("This program shows the number you entered is a leap year or not.")
user_in = input("Enter there the number: ")
try:
    year = int(user_in)
except ValueError:
    msg = "Incorrect data, you have to enter a number!"
except NameError as Nerr:
    print("Incorrect data: " + Nerr + ". You have to enter a number!")
except TypeError:
    print("Incorrect data! You have to enter a number!")
if year == str(user_in):
    msg = "Incorrect data: " + user_in + ", You have to enter a number!"
elif year / 100 == year // 100: 
    msg = "It is not a leap year."
elif year / 4 == year // 4:
    msg = "It is a leap year."
else:
    msg = "It is not a leap year." 
print(msg)