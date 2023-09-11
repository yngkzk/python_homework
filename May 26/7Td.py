print("Enter your current time.")
hours = input("Hour: ")
minutes = input("Minute: ")
x = 23
y = 60
try:
    z = int(hours)
    n = int(minutes)
except ValueError:
    message = "Incorrect data"
else:
    result_h = x - z
    result_m = y - n 
    message = "The next day will start in: ", result_h, "hours, and", result_m, "minutes!"
print(message)