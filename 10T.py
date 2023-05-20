# 10. Зарплата работника составляет $250 + 10% от продаж. Запросите общую сумму продаж за месяц и посчитайте зарплату.
# $250 + 10%
mny = input("Enter your total monthly sales: ")
m = int(mny)
x = 250
y = m // 10
result = 250 + y
print("Your wage is: $", result, sep="")
