import threading
import os


def set_vowel_upper(*args):
    global new_text
    new_text = list(args)
    for i in range(len(new_text)):
        if new_text[i] in 'oeiua':
            new_text[i] = new_text[i].capitalize()
    new_text = map(str, new_text)
    new_text = ''.join(new_text)
    return new_text


lock = threading.Lock()
file_names = ['text_files/test_text_one.txt',
              'text_files/test_text_two.txt',
              'text_files/test_text_three.txt',
              'text_files/test_text_four.txt',
              'text_files/test_text_five.txt']

for x in range(len(file_names)):
    new_text = ''
    my_file = open(f'{file_names[x]}', 'r+', encoding='utf-8')
    text = my_file.read()
    thread = threading.Thread(target=set_vowel_upper, args=text)
    thread.start()
    thread.join()
    if new_text != text:
        my_file.write(new_text)
        os.rename(file_names[x], f'{file_names[x][:-4]}_modified.txt')
    my_file.close()

