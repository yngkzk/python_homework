# 9**.  Пользователь вводит строку любой длины и целове число N.
# Вывести строку, которая состоит из повторяющихся фрагментов строки пользователя, длиной N символов. 
# Например, если пользователь ввёл "fido" и число 10, результатом будет строка "fidofidofi". НЕ использовать циклы!
user_in_str = input("Enter there your string: ")
string = str(user_in_str)
user_in_numb = input("Enter how many symbols you want to see: ")
counts = int(user_in_numb)
result = (string * counts)[:counts]
print("This is your result: ", result)

