my_list = input('Enter numbers separated by ",": ')
my_list = my_list.split(',')


def check_list(new_list):
    if len(new_list) > 10:
        new_list = new_list[0:10]
        return new_list
    if len(new_list) < 10:
        print('You have to enter 10 numbers.')
        new_list = input('Enter numbers separated by ",": ')
        new_list = new_list.split(',')
        return check_list(new_list)


def is_even(numbers):
    even_list = []
    for i in range(len(numbers)):
        if numbers[i] % 2:
            continue
        else:
            even_list.append(numbers[i])
    return even_list


checked_list = check_list(my_list)
checked_list = [int(i) for i in checked_list]
checked_number_list = is_even(checked_list)
print(checked_number_list)
