user_in = '24,6,12,6,12,6,5,2'
my_list = user_in.split(',')

my_list = list(map(int, my_list))


def bubble_sort(val, key=None):
    value = val.copy()
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(value) - 1):
            if value[i] > value[i + 1]:
                value[i], value[i + 1] = value[i + 1], value[i]
                is_sorted = False
            else:
                continue
    if key:
        new_value = []
        low_value = []
        for x in range(len(value)):
            if not key(value[x]):
                low_value.append(value[x])
            elif key(value[x]) is True:
                new_value.append(value[x])
            else:
                new_value.append(key(value[x]))
        return new_value + low_value
    else:
        return value


print(my_list)
print(bubble_sort(my_list))
print(bubble_sort(my_list, key=lambda x: x ** 2))
print(bubble_sort(my_list, key=lambda x: x > 7))
