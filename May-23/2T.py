# 2. Нумерология. Запросите у пользователя слово из трёх букв и выведите сумму кодов всех символов в этом слове. Для нахождения кода символа используйте функцию ord().
user_in_str = input("Enter your three letter word: ")
sym1 = user_in_str[0]
s1 = ord(sym1)
sym2 = user_in_str[1]
s2 = ord(sym2)
sym3 = user_in_str[2]
s3 = ord(sym3)
result = s1 + s2 + s3
print("Your sum of codes of all symbols of this word: ", result)
