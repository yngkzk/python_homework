print("This program shows is your word palindrome or not.")
user_in = input("Enter your 5 letter word: ")
try:
    users_word = str(user_in)
    first = users_word[0]
    second = users_word[1]
    fourth = users_word[3]
    fifth = users_word[4]
except ValueError:
    msg = "Incorrect data, you have to enter a word!"
except IndexError:
    msg = "Incorrect data, you have to enter a word!"
except NameError as Nerr:
    print("Incorrect data: " + Nerr + ". You have to enter a word!")
if first == fifth and second == fourth:
    msg = "Your word is palindrome"
else:
    first != fifth or second != fourth
    msg = "Your word is not palindrome"
print(msg)