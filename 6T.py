# 6. Пользователь вводит значения a и b для формулы a * x + b = 0, а программа считает и выводит значение x.
print("Here is the formula for you: a * x + b = 0")
users_numb = input("Enter a value for 'a': ")
users_numb2 = input("Enter a value for 'b': ")
a, b = int(users_numb), int(users_numb2)
given_formula = -b / a
print("Your 'X' is equals to: ", given_formula)
