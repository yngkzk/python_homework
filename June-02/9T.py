def sum_divisors(num, i=1, total=0): # В интернете посмотрел, это для себя
    if i == num:
        if total == num:
            return True
        else:
            return False
    if num % i == 0:
        total += i
    return sum_divisors(num, i+1, total)
    if int(num) < 1:
        return False
    else:
        return "Result"
    return sum_divisors(num)

num = sum_divisors(28)
print(num)