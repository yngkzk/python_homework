# 9. Запросите у пользователя пятизначное число и переместите последнюю цифру в начало (из числа 12345 должно получиться число 51234). Задачу решить математически!
fdn = input("Enter five digit number: ")
x = int(fdn)
n = x % 10
f = str(n)
r = x // 10
t = str(r)
result = f + t
print("Your result is: ", result)
