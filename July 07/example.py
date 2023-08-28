clothes = {'t-shirts': 2, 'shorts': 3, 'pants': 2, 'sweaters': 4}  # Make a simple dictionary

total_quantity = sum(clothes.values())  # Find total number of clothes

print('Total Q:', total_quantity, sep=' ')  # Print result

max_value = max(clothes.values())  # Calculate the most popular object in dictionary
modus_clothes = list(clothes.keys())[list(clothes.values()).index(max_value)]  # Get key by value in dictionary

print(modus_clothes)  # Print result
