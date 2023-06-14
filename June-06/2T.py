def get_day_of_the_week(answer, num = 1):
    if answer == "yes":
        if num == 1:
            message = "The day of the week: Monday."
        if num == 2:
            message = "The day of the week: Tuesday."
        if num == 3:
            message = "The day of the week: Wednesday."
        if num == 4:
            message = "The day of the week: Thursday."
        if num == 5:
            message = "The day of the week: Friday."
        if num == 6:
            message = "The day of the week: Saturday."
        if num == 7:
            message = "The day of the week: Sunday."
        print(message)
        answer = input("You want to continue? (yes/no): ")
        return get_day_of_the_week(answer, num+1)
    else:
        print("Result.")
print("This program shows days of the weeks.")
user_in = input("You want to start? (yes/no): ")
get_day_of_the_week(user_in)