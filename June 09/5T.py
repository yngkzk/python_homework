user_in = input("Enter a number: ")
user_in_move = input("How many numbers do you want to shift? ")

index = int(user_in_move)
last_numbers = ""
first_numbers = ""

for i in user_in:
    index -= 1
    if index >= 0:
        last_numbers  += str(i)
    else:
        first_numbers += str(i)
result = str(first_numbers) + str(last_numbers)
print(result)