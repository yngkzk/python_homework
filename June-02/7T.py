def get_seconds(user_in1 = None, user_in2 = None, user_in3 = None):
    user_in1 = str(user_in1).zfill(1)
    user_in2 = str(user_in2).zfill(1)
    user_in3 = str(user_in3).zfill(1)
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
print(get_seconds(user_in1, user_in2, user_in3))