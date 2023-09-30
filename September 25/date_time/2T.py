import datetime


def add_time(func):
    def wrapper():
        today = datetime.datetime.today()
        return f'[{today.year}-{today.month}-{today.day}] {func()}'
    return wrapper


@add_time
def logger_debug():
    return 'Debug message'


print(logger_debug())


