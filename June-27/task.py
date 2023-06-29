from functools import reduce


my_float_numbers = [2.32, 6.77, 1.1221, 3.412, 32.89, 63, 12, 3, 76.112, 8, 9]


def square_and_round(num):
    num *= num
    return round(num, 3)


map_result = list(map(square_and_round, my_float_numbers))
print(map_result)


my_names = ['Piko', 'Magniy-B6', 'Example', 'Medium', 'Reallylongname', 'Zombie-killer']


def get_len(word):
    if len(word) < 7:
        return True
    else:
        return False


filter_result = list(filter(get_len, my_names))
print(filter_result)


my_numbers = [2, 2, 3, 4]


reduce_result = reduce(lambda x, y: x * y, my_numbers)
print(reduce_result)
