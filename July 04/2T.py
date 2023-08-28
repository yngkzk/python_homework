my_file = open('input.txt', encoding='utf-8')
text = my_file.read()
my_file.close()


def get_syllables(word):
    new_text = ''
    for i in range(len(word)):
        vowels = 'оаие'
        if word[i] in vowels:
            new_text = word[i] + '-'
        else:
            new_text += word[i]
    return new_text


def cut_hyphen(word):
    current_word = word.split('\n')
    new_text = ''
    for x in range(len(current_word)):
        if current_word[x].endswith('-'):
            new_text += '\n' + current_word[x][:-1]
        else:
            new_text += '\n' + current_word[x]
    return ''.join(new_text)


another_text = list(map(get_syllables, text))
finished_text = ''.join(another_text)
filtered_text = cut_hyphen(finished_text)
print(text)
print(filtered_text)
