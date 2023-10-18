import random


def generate_random(range, max):
    current = 1
    while current <= max:
        yield random.randint(0, range)
        current += 1


for number in generate_random(5, 4):
    print(number)