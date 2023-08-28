my_list = [9, 23, -22, 0, 33, -12, 4, 6, 21, 2]
# my_list = [-22, 1, 5, 34, 12, 11, 42]
low_value = float('inf')    # Два списка на всякий, проверить
high_value = 0


for i in range(len(my_list)):
    if my_list[i] < low_value:
        low_value = my_list[i]
    if my_list[i] > high_value:
        high_value = my_list[i]


first_object = my_list.index(low_value)
second_object = my_list.index(high_value)

first_popped = my_list.pop(first_object)
second_popped = my_list.pop(second_object-1)

first_inserted = my_list.insert(first_object, high_value)
second_inserted = my_list.insert(second_object, low_value)

print(low_value, high_value)
print(my_list)
print(first_object, second_object)
