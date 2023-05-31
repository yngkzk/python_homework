print("This program shows the number you entered is a leap year or not.")
user_in = input("Enter there the number: ")
try:
    year = str(user_in)
    div1 = year / 4
    div01 = year // 4
    div2 = year / 100 
    div02 = year // 100
except ValueError:
    msg = "Incorrect data, you have to enter a number!"
except NameError as Nerr:
    print("Incorrect data: " + Nerr + ". You have to enter a number!")
except TypeError:
    print("Incorrect data! You have to enter a number!")
if div2 == div02:
    msg = "It is not a leap year."
elif div1 == div01:
    msg = "It is a leap year."
else:
    msg = "It is not a leap year."
print(msg)