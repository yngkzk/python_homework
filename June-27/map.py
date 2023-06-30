my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))

print(results)


my_list = ['for', 'Example', 'this', 'text']
converted_list = list(map(str.lower, my_list,))
sorted_list = sorted(converted_list, reverse=False, key=None)
# VN:                                ^^^^^^^^^^^^^^^^^^^^^^^
# если вы используете значения по умолчанию, то их не обязательно указывать, т.е.
# можно просто написать sorted(converted_list)
print(converted_list, sorted_list)
