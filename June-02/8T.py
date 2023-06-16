def convert_seconds(user_in1):
    hours   = int(user_in1) // (60 * 60)
    minutes = (int(user_in1) - hours * (60 * 60)) // 60
    seconds = (int(user_in1) - hours * (60 * 60) - minutes * 60)
    form = ("Your data from seconds to daytime: %02d:%02d:%02d.")
    message = form % (hours, minutes, seconds)
    return message
print("This program converts your data from seconds to daytime in this format 'hh:mm:ss'.")
user_in1 = input("Enter the seconds: ")
print(convert_seconds(user_in1))