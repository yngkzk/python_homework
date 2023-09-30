import datetime
import time


def reminder(task, seconds):
    now = datetime.datetime.now()
    second = now.second
    match second:
        case s if 20 < s < 30:
            print('Че делать')
            x_seconds = seconds + 10
        case s if 30 < s < 40:
            print('Я сюда попал?')
            x_seconds = seconds + 5
        case _:
            x_seconds = seconds

    while True:
        now = datetime.datetime.now()
        second = now.second
        if second == x_seconds:
            return f"It's time to {task}"
        else:
            time.sleep(0.4)


print(reminder('finish homework', 25))
