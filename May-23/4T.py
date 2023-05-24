# 4. Половинки. Пользователь вводит слово любой длины. Разбейте это слово пополам и выведите обе его половины через пробел.
user_in_str = input("Enter there your word: ")
words_len = len(user_in_str)
symb = words_len // 2
cut1 = user_in_str[:symb]
cut2 = user_in_str[-symb:]
result = cut1 + " " + cut2
print("This is your cut word: ", result)
