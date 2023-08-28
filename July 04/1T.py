text = "dsnaldsands@gmail.com nds@kalnd dks@land klsand@mail.ru klsadnlk sa@gmail.com"

text = text.split()


def find_email(word):
    if '@' in word:
        if word.endswith(('com', 'ru', 'edu')):
            return True
    else:
        return False


new_text = filter(find_email, text)
print(list(new_text))

