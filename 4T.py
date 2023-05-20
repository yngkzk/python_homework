# 4. Реализуйте конвертор из километров в мили (пользователь вводит километры, программа выводит мили). 1 км = 0,621371 миль.
number_req = input("Enter the number you want to convert to miles: ")
number = int(number_req)
convertator = 0.621371
result = number * convertator
print("Your number in miles: ", result)
