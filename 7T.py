# 7. Запросите у пользователя текущее время (часы и минуты) и выведите, сколько часов и минут осталось до следующего дня.
print("Enter your current time.")
hours = input("Hour: ")
minutes = input("Minute: ")
x = 23
y = 60
z = int(hours)
n = int(minutes)
result_h = x - z
result_m = y - n 
print("The next day will start in: ", result_h, "hours, and", result_m, "minutes!")