user_in = '24,6,12,6,12,6,5,2'
my_list = user_in.split(',')

my_list = list(map(int, my_list))


def select_sort(val, key=None):
    value = val.copy()
    new_list = []
    for _ in range(len(value)):
        min_index = 0
        for k in range(1, len(value)):
            if value[k] < value[min_index]:
                min_index = k
        new_list.append(value[min_index])
        del value[min_index]
    if key:
        new_value = []
        low_value = []
        for x in range(len(new_list)):
            if not key(new_list[x]):
                low_value.append(new_list[x])
            elif key(new_list[x]) is True:
                new_value.append(new_list[x])
            else:
                new_value.append(key(new_list[x]))
        return new_value + low_value
    else:
        return new_list


print(my_list)
print(select_sort(my_list))
print(select_sort(my_list, key=lambda x: x > 13))
print(select_sort(my_list, key=lambda x: x * 2))
