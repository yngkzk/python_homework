def get_sum(user_in):
    if int(user_in):
        if int(num) > 0:
        # VN: Здесь программа падает - нет переменной с именем num
            print(num)
            return num + get_sum(num-1)
        else:
            print("The sum of these numbers is.")
            return 0
        return num
    else:
        return "No input entered."
print("This program shows the sum of the numbers from 0 to the entered number.")
user_in = input("Enter the number: ")
print(get_sum(user_in))