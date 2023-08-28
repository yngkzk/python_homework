# 8. Запросите у пользователя трехзначное число и выведите вторую цифру этого числа. Для решения задачи используйте оператор % (остаток от деления).
tdn = input("Enter three digit number: ")
n = int(tdn)
result = n % 100
result2 = result // 10
print("The middle of the number equals: ", result2)

