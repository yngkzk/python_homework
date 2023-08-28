result = ""
number = 0

for i in range(32, 126+1):
    number += 1
    if number >= 5:
        result += str(i) + " - " + chr(i) + "\n"
        print(result)
        result = ""
        number = 0
    else:
        result += str(i) + " - " + chr(i) + ", "