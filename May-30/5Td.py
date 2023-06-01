print("This program converts the currency from USD to EUR, UAN or AZN.")
user_in = input("Enter your value in USD: ")
user_in_cur = input("Enter the currency to which you want to transfer (EUR, UAN or AZN): ")
UAN = 7.1068
AZN = 1.69
EUR = 0.936899799
try:
    usd = float(user_in)
except ValueError:
    msg = "Incorrect data."
except NameError as Nerr:
    print("Incorrect data: " + Nerr + ". You have to enter a value!")
if usd == str(user_in):
    msg = "Incorrect data: " + user_in + ", You have to enter a number!"
elif usd < 0:
    msg = "Value can not be negative."
elif user_in_cur == "EUR":
    usd_to_eur = usd * EUR
    msg = "Here is your result in EUR: ", usd_to_eur
elif user_in_cur == "UAN":
    usd_to_uan = usd * UAN
    msg = "Here is your result in UAN: ", usd_to_uan
elif user_in_cur == "AZN":
    usd_to_azn = usd * AZN
    msg = "Here is your result in AZN: ", usd_to_azn
else:
    print("Result.")
print(msg)