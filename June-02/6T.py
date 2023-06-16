def get_time(user_in1=0, user_in2=0, user_in3=0):
    if user_in1 == 0 and user_in2 == 0 and user_in3 == 0:
        return "Your time in the format: 00:00:00."
    elif user_in1 and user_in2 and user_in3:
        if int(user_in1) < 10:
            hours   = "0" + str(user_in1)
        else:
            hours = str(user_in1)
        if int(user_in2) < 10:
            minutes = "0" + str(user_in2)
        else:
            minutes = str(user_in2)
        if int(user_in3) < 10:
            seconds = "0" + str(user_in3)
        else:
            seconds = str(user_in3)
        template = "Your time in the format: %s:%s:%s."
        message = template % (hours, minutes, seconds)
        return message
    else:
        return "Incorrect data."

print("This program converts your data into a string in this format 'hh:mm:ss'.")
user_in1 = input("Enter a hour: ")
user_in2 = input("Enter a minute: ")
user_in3 = input("Enter a second: ")
print(get_time(user_in1, user_in2, user_in3))