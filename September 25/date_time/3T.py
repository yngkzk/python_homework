import datetime
import time


def take_action():
    now = datetime.datetime.now()
    second = now.second
    match second:
        case second if second < 30: x_seconds = second + 10
        case second if second < 40: x_seconds = second + 5
        case _: x_seconds = second
    while True:
        now = datetime.datetime.now()
        second = now.second
        if second == x_seconds:
            return 'Its time to shine'
        else:
            time.sleep(0.4)


print(take_action())


