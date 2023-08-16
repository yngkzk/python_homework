user_in = '6,3,7,2,9,0,8,1'
my_list = user_in.split(',')

my_list = list(map(int, my_list))


def quick_sort(val, key=None):
    value = val.copy()
    if len(value) <= 1:
        return value
    pivot = value[0]
    less = list(filter(lambda x: x < pivot, value))
    equals = [i for i in value if i == pivot]
    more = list(filter(lambda x: x > pivot, value))
    result = quick_sort(less) + equals + quick_sort(more)
    if key:
        new_value = []
        low_value = []
        for x in range(len(result)):
            if not key(result[x]):
                low_value.append(result[x])
            elif key(result[x]) is True:
                new_value.append(result[x])
            else:
                new_value.append(key(result[x]))
        return new_value + low_value
    else:
        return result


print(my_list)
print(quick_sort(my_list))
print(quick_sort(my_list, key=lambda x: x > 2))
print(quick_sort(my_list, key=lambda x: x * 2))
