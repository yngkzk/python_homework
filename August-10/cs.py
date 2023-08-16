print('x^2 (2y + 5z).')

x = float(input('1: '))
y = float(input('2: '))
z = float(input('3: '))

example = x ** 2 * (2 * y + 5 * z)

print(example)

age = 12
print(age)


first = 'programming'
second = list(first)
element = 'c'
second.insert(1, element)
finished = ''.join(map(str, second))
print(finished)

N = 10

synonyms = {}

for i in range(N):
    word1 = input("Введите слово: ")
    word2 = input("Введите его синоним: ")
    synonyms[word1] = word2

    print("\nСловарь синонимов:")
    for word, synonym in synonyms.items():
        print(f"{word}: {synonym}")

synonyms = {'cui': 'ds', 2: 32, '': 0}

for word, synonym in synonyms.items():
    print(f"{word}: {synonym}")
