print("This program shows what types of numbers you have entered.")
positive = 0
negative = 0
even     = 0
odd      = 0
zero     = 0
for i in range(0, 10):
    user_in = float(input('Enter a number: '))
    if user_in > 0:
        positive   += 1
        if user_in % 2 == 0:
            even       += 1
        if user_in % 2:
            odd        += 1
    elif user_in < 0:
        negative   += 1
        if user_in % 2 == 0:
            even       += 1
        if user_in % 2:
            odd        += 1
    elif user_in == 0:
        zero       += 1
    else:
            print("Result is.")
message = ("%s - positive, %s - negative, %s - even, %s - odd and %s - zero, numbers.") % (positive, negative, even, odd, zero)
print(message)