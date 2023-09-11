my_list = [3, 9, 8, 4, 5, 1, 4, 6, 12, 4, 2, 1, 61]
new_list = []

for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        new_list.append(my_list[i+1])

print(new_list)
