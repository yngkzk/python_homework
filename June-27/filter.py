scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def is_a_student(score):
    return score > 75


over_75 = list(filter(is_a_student, scores))

print(over_75)


dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)
