user_in = 'hello,this,is,a,test'
my_list_numbers = [2, -5, 4, -12, 2, 1, 8, 4]
my_list = user_in.split(',')

my_list = list(map(str, my_list))


def bubble_sort(val, key=None):
    value = val.copy()
    is_sorted = False
    if key is None:
        key = lambda x: x
    while not is_sorted:
        is_sorted = True
        for i in range(len(value) - 1):
            if key(value[i]) > key(value[i + 1]):
                value[i], value[i + 1] = value[i + 1], value[i]
                is_sorted = False
            else:
                continue
    return value


print(my_list)
print(bubble_sort(my_list))
print(bubble_sort(my_list, key=len))
print(bubble_sort(my_list_numbers, key=lambda x: x * 7))
print(bubble_sort(my_list_numbers, key=abs))
