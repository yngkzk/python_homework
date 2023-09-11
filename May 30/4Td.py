print("This program shows is your word palindrome or not.")
user_in = input("Enter your 5 letter word: ")

try:
    user_in = str(user_in)
    users_word = str(user_in)
    length = len(users_word)
except ValueError:
    msg = "Incorrect data, you have to enter a word!"
else:
    if length > 5:
        msg = "Your word has more, than 5 letters."
    elif length < 5:
        msg = "Your word has less, than 5 letters."
    else:
        first = users_word[0]
        second = users_word[1]
        fourth = users_word[3]
        fifth = users_word[4]
        if first == fifth and second == fourth:
            msg = "Your word is palindrome"
        else:
            msg = "Your word is not palindrome"
print(msg)