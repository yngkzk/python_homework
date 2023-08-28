# 7. Дата. Запросите у пользователя год, месяц и число его рождения, и выведите эту дату в формате "дд.мм.гггг".
# Например, если пользователь вводит числа 1999, 3 и 1, программа должна вывести "01.03.1999".
# Подсказка: используйте сложные метки для подстановки.
print("Fill in your birth data fields!")
year = input("Year: ")
month = input("Month: ")
day = input("Day: ")
year, month, day = str(year), str(month), str(day)
form = "Your date of birth is: '0%s.0%s.%s' "
result = form % (day, month, year)
print(result)

