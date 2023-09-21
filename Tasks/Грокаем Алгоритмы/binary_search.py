def binary_search(given_list, item):  # O(log n)
    low = 0
    high = len(given_list)-1

    while low <= high:
        mid = (low+high)
        guess = given_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
