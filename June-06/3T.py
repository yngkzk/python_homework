def get_multiplication_table(number=2, multiplier=1):
    if number < 10:
        if multiplier == 11:
            return get_multiplication_table(number+1)
        table_multiple = number * multiplier
        print(str(number) + " * " + str(multiplier) + " = " + str(table_multiple))
        return get_multiplication_table(number, multiplier+1)
    return
print("This program shows multiplication table from 2 to 9.")
get_multiplication_table(2, 1) 