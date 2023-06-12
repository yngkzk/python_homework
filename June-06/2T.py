def get_day_of_the_week(answer, num = 1):
    if answer == "yes":
        if num == 1:
            print("The day of the week: Monday.")
            answer = input("You want to continue? (yes/no): ")
            return get_day_of_the_week(answer, num+1)
        if num == 2:
            print("The day of the week: Tuesday.")
            answer = input("You want to continue? (yes/no): ")
            return get_day_of_the_week(answer, num+1)
        if num == 3:
            print("The day of the week: Wednesday.")
            answer = input("You want to continue? (yes/no): ")
            return get_day_of_the_week(answer, num+1)
        if num == 4:
            print("The day of the week: Thursday.")
            answer = input("You want to continue? (yes/no): ")
            return get_day_of_the_week(answer, num+1)
        if num == 5:
            print("The day of the week: Friday.")
            answer = input("You want to continue? (yes/no): ")
            return get_day_of_the_week(answer, num+1)
        if num == 6:
            print("The day of the week: Saturday.")
            answer = input("You want to continue? (yes/no): ")
            return get_day_of_the_week(answer, num+1)
        if num == 7:
            print("The day of the week: Sunday.")
            answer = input("You want to continue? (yes/no): ")
            return get_day_of_the_week(answer, num-6)
    else:
        print("Result.")
print("This program shows days of the weeks.")
user_in = input("You want to start? (yes/no): ")
get_day_of_the_week(user_in)