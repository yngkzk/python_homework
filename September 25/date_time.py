import datetime
# Важно не указать название своего файла, как datetime.py, иначе python не поймет что вы хотите импортировать


now = datetime.datetime.now()
print(now)

print(now.year, now.month, now.day)


birthday = datetime.date(2004, 11, 20)
today = datetime.datetime.today()

age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

print('Age - ', age, sep='')


def decorator_function(func):
    def wrapper():
        print('Выполняется декоратор')
        func()
    return wrapper


@decorator_function
def hello():
    print('Hello, World!')


hello()
