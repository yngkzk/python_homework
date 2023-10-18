import time
import string
import hashlib
from functools import lru_cache


class Hacker:
    loop = None
    hash_md5 = ''
    last_hash = ''

    def __init__(self, hash_md5):
        self.hash_md5 = hash_md5

    @lru_cache(maxsize=5)
    def _find_password(self, symb):
        hash = hashlib.md5()
        hash.update(symb.encode('utf-8'))
        password = hash.hexdigest()
        if password == self.hash_md5:
            print(f'Success! {symb}')
            self.loop = False
            return 

    def measuretime(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print('Elapsed time:', round((end_time - start_time)*100), 'ms', sep=' ')
        return wrapper

    @measuretime
    def hack(self):
        spec_symbols = '~!@#$%^&*()_+-='
        letters = string.ascii_letters
        numbers = '0123456789'

        symbols = numbers + letters + spec_symbols
        self.loop = True

        for x in symbols:
            if self.loop is False:
                print(self._find_password.cache_info())
                break
            else:
                for y in symbols:
                    for z in symbols:
                        for f in symbols:
                            template = f'{x}{y}{z}{f}'
                            self._find_password(template)


myHack = Hacker('ebec4c0d4133e6ea7d83f7137cefa6a5')
myHack.hack()