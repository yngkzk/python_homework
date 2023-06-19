print("This program shows the resulting number and how many divisions were made by 2.")
user_in = int(input("Enter a number: "))
num = user_in
div = 2
tries = 0
while num > 50:
    num /= div
    tries += 1
    print(num, tries)
