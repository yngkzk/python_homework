print("This program shows the number you entered is a leap year or not.")
user_in = input("Enter there the number: ")
try:
    user_in = int(user_in)
    year = user_in
except ValueError:
    msg = "Incorrect data, you have to enter a number!"
# VN: обработка NameError и TypeError здесь не нужны. 
# Эти два класса ошибок относятся к ошибкам программиста, а не пользователя)
# VN: а) странное условие; б) в этом месте программа падает, если пользователь ввёл не число
# VN: Если год делится на 100, он может быть високосным. Например, 2000 год. Точное условие дано в дз
elif year / 100 == year // 100: 
    msg = "It is not a leap year."
elif year / 4 == year // 4:
    msg = "It is a leap year."
else:
    msg = "It is not a leap year." 
print(msg)