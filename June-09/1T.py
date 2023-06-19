print("This program shows the sum of all numbers in a user-specified range")
user_in  = int(input("Enter first number: " ))
user_in2 = int(input("Enter second number: "))
sums = 0
for i in range(user_in, user_in2+1):
    sums += i
message = "Result is = " + str(sums)
print(message)