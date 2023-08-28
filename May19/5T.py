# 5. Реализуйте калькулятор. Пользователь вводит два числа, а программа выводит результаты действий + - * / между этими числами.
users_numb = input("Enter the first number: ")
users_numb2 = input("Enter the second number: ")
n1 = int(users_numb)
n2 = int(users_numb2)
res1 = n1 + n2
res2 = n1 - n2
res3 = n1 * n2
res4 = n1 / n2
print("The result of your action: ", "Addition: ", res1, "Subtraction: ", res2, "Multiplication: ", res3, "Division:", res4)

