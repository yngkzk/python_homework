# 6. Кинотеар. Напишите программу, которая считывает с клавиатуры последовательно три строки: название фильма, название кинотеатра и время, после чего выводит на экран «Билет на [название фильма] в [название кинотеатра] на [время] забронирован.»
# Подсказка: используйте операцию подстановки для строк.
print("Hello, please fill in fields below to create your cinema ticket!")
films_name = input("The name of the film: ")
cinemas_name = input("The name of the cinema where you want to watch the film: ")
time = input("Approximate time you would like to watch the film: ")
time = str(time)
form = "You created your cinema ticket! The film '%s', in the cinema '%s' - booked for this time '%s'."
data = form % (films_name, cinemas_name, time)
print(data)

