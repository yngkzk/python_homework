def get_time_to_seconds_from_user(user_in1 = None, user_in2 = None, user_in3 = None):
    user_in1 = str(user_in1).zfill(1)
    user_in2 = str(user_in2).zfill(1)
    user_in3 = str(user_in3).zfill(1)
    if int(user_in1) < 0:
        message = "Your number cannot be negative!"
        return message
    if int(user_in2) < 0:
        message = "Your number cannot be negative!"
        return message
    if int(user_in3) < 0:
        message = "Your number cannot be negative!"
        return message
    if int(user_in1) or int(user_in2) or int(user_in3):
        hours   = int(user_in1) * 60 * 60
        minutes = int(user_in2) * 60
        seconds = int(user_in3)
        total_seconds = int(hours) + int(minutes) + int(seconds)
        message = "Your time in seconds: " + str(total_seconds)
        return message
    else:
        return "No input entered."
print("This program converts your data from daytime to seconds.")
user_in1 = input("Enter a hour: ")
user_in2 = input("Enter a minute: ")
user_in3 = input("Enter a second: ")
print(get_time_to_seconds_from_user(user_in1 or "", user_in2 or "", user_in3 or ""))