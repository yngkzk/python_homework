# Напишите программу, которая методом прямого перебора подберёт пароль, соответствующий хэшу MD5: 'ebec4c0d4133e6ea7d83f7137cefa6a5'.
# Пароль имеет длину 8 символов, в пароле могут использоваться английские буквы в нижнем и верхнем регистре, цифры и спецсимволы из ряда: "~!@#$%^&*()_+-=".
# Измерьте время подбора пароля с помощью функции time() модуля time.
import hashlib
import time
import string
 

def find_password(symb):
    hash = hashlib.md5()
    hash.update(symb.encode('utf-8'))
    password = hash.hexdigest()
    if password == hash_md5:
        print(f'Success! {template}')
        global loop
        loop = False
        return 

start_time = time.time()

spec_symbols = '~!@#$%^&*()_+-='
letters = string.ascii_letters
numbers = '0123456789'
hash_md5 = 'ebec4c0d4133e6ea7d83f7137cefa6a5'

symbols = numbers + letters + spec_symbols
loop = True


for x in symbols:
    if loop is False:
        break
    else:
        for y in symbols:
            for z in symbols:
                for f in symbols:
                    template = f'{x}{y}{z}{f}'
                    find_password(template)


end_time = time.time()

elapsed_time = end_time - start_time
print('Elapsed time:', round(elapsed_time, 4), 'seconds', sep=' ')