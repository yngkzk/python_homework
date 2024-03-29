user_in = 'hello,this,is,a,test'
my_list_numbers = [2, 5, 4, 12, 2, 1, 8, 4]
my_list = user_in.split(',')

my_list = list(map(str, my_list))


def quick_sort(val, key=None):
    value = val.copy()
    if len(value) <= 1:
        return value
    if key is None:
        key = lambda x: x
    pivot = value[0]
    less = list(filter(lambda x: key(x) < key(pivot), value))
    equals = [i for i in value if key(i) == key(pivot)]
    more = list(filter(lambda x: key(x) > key(pivot), value))
    result = quick_sort(less) + equals + quick_sort(more)
    return result


print(my_list)
print(quick_sort(my_list))
print(quick_sort(my_list, key=len))
print(quick_sort(my_list_numbers, key=lambda x: x ** 2))
