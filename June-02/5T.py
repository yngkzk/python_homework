def get_ints_from_user(user_in1, user_in2):
    r = float(user_in1) / 2
    h = float(user_in2)
    V = 3.14 * (r ** 2) * h
    V_liters = V * 1000
    form = "Its your volume in liters: %.2f"
    message = form % V_liters
    return message
print("This program shows the value of the tank in liters.")
user_in1 = input("Enter diameter of the tank(m): ")
user_in2 = input("Enter height of the tank(m): ")
print(get_ints_from_user(user_in1, user_in2))