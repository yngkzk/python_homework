first_list = [2, 'another word', 1, 5, 'word', 643, 12, 6, 1, 22]
second_list = [2, 'word', 643, 22]

new_list = first_list.copy()

for i in range(len(new_list)):
    for x in range(len(second_list)):
        if new_list[i] is second_list[x]:
            first_list.remove(second_list[x])

print(first_list)
