# 10** Запросить у пользователя слово на английском языке, и вывести его написание с большой буквы. 
# НЕ использовать методы для преобразования регистра!
user_in = input("Enter your word in english with a small first letter: ")
user_in_letter = user_in[:1]
user_in_word = user_in[1:]
go_to_number = ord(user_in_letter)
go_to_number = int(go_to_number)
converting = go_to_number - 32
back_to_letter = chr(converting)
form = "Your word with a capital first letter: " + "%s" + user_in_word
result = form % (back_to_letter)
print(result)
