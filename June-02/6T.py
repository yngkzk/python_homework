def get_time(user_in1 = None, user_in2 = None, user_in3 = None):
    user_in1 = str(user_in1).zfill(1)
    user_in2 = str(user_in2).zfill(1)
    user_in3 = str(user_in3).zfill(1)
    if int(user_in1) or int(user_in2) or int(user_in3):
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
print(get_time(user_in1 or "", user_in2 or "", user_in3 or ""))