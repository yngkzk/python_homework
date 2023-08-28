# 9. Запросите у пользователя пятизначное число и переместите последнюю цифру в начало (из числа 12345 должно получиться число 51234). Задачу решить математически!
fdn = input("Enter five digit number: ")
x = int(fdn)
lastn = x % 10
fourn = x // 10
f = lastn * 10000
t = fourn
result = f + t
print("Your result is: ", result)

