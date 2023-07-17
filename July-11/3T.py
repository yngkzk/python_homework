import string

with open('text.txt', 'r', encoding='utf-8') as my_file:
    text = my_file.read()


chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
key = key[::-1]
empty_text = ''

for letter in text:
    index = key.index(letter)
    empty_text += chars[index]

with open('text.txt', 'w', encoding='utf-8') as my_file:
    my_file.write(empty_text)
