def get_multiplication_table(number, multiplier=2):
    if number > 0 and number < 11:
        if multiplier <= 9:
            result = number * multiplier
            print("Multiplication by", multiplier, "=", result, sep=" ")
            return get_multiplication_table(number, multiplier+1)
        else:
            return "Result."
    else:
        print("Number out of range.")
        return       
print("This program shows multiplication table from 2 to 9. Enter a number between 1 and 10.")
user_in = int(input("Enter the number: "))
get_multiplication_table(user_in)