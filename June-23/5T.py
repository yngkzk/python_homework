my_list = [9, 23, -22, 0, 33, -12, 4, 6, 21, 2]
# my_list = [-22, 1, 5, 34, 12, 11, 42]
low_value = float('inf')    # Два списка на всякий, проверить
high_value = 0


for i in range(len(my_list)):
    if my_list[i] < low_value:
        low_value = my_list[i]
    if my_list[i] > high_value:
        high_value = my_list[i]

first_index = my_list.index(low_value)
second_index = my_list.index(high_value)

if first_index > second_index:
    distance = first_index - second_index
else:
    distance = second_index - first_index

print(low_value, high_value)
print(first_index, second_index)
print(distance)
