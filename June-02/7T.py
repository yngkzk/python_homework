def get_seconds(user_in1 = 0, user_in2 = 0, user_in3 = 0):
    if user_in1 or user_in2 or user_in3:
        hours   = int(user_in1) * 60 * 60
        minutes = int(user_in2) * 60
        seconds = int(user_in3)
        total_seconds = hours + minutes + seconds
        return total_seconds
    else:
        return "No input entered."
print("This program converts your data from daytime to seconds.")
user_in1 = input("Enter a hour: ")
user_in2 = input("Enter a minute: ")
user_in3 = input("Enter a second: ")
print(get_seconds(user_in1, user_in2, user_in3))