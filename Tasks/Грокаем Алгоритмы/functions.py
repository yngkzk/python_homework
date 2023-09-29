def count_elements(arr, n=0):
    if arr == []:
        return 0
    return 1 + count_elements(arr[:-1])
    
print(count_elements([2, 5, 7, 1, 2, 6, 8, 2]))


def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(max([2, 5, 7, 1, 2, 6, 8, 2]))