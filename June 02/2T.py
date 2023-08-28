def sum_nums(n):
    if n == 0:
        return 0
    else:
        return n + sum_nums(n-1)
        
print("This program shows the sum of the numbers from 0 to the entered number.")
user_in = int(input("Enter the number: "))
print(sum_nums(user_in))