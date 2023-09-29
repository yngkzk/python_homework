def sum(arr):
    total = 0
    for x in range(len(arr)):
        total += arr[x]
    return total

print(sum([2, 6, 7, 2]))