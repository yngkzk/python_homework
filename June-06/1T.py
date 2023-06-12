def print_smileys(n):
    if int(n) > 0:
        print(" :) ")
        return print_smileys(int(n)-1)
    else:
        return "Result."
print("This program shows the number of emoticons you want to see")
user_in = input("Enter the number: ")
print_smileys(user_in)