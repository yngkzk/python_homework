user_in = 'hello,this,is,a,test'
my_list_numbers = [2, 5, 4, 12, 2, 1, 8, 4]
my_list = user_in.split(',')

my_list = list(map(str, my_list))


def select_sort(val, key=None):
    value = val.copy()
    new_list = []
    if key is None:
        key = lambda x: x
    for _ in range(len(value)):
        min_index = 0
        for k in range(1, len(value)):
            if key(value[k]) < key(value[min_index]):
                min_index = k
        new_list.append(value[min_index])
        del value[min_index]
    return new_list


print(my_list)
print(select_sort(my_list, key=len))
print(select_sort(my_list_numbers, key=lambda x: x / 2))
