import datetime
import time
import calendar


def timing(day=0, weeks=0, month=0):
    today = datetime.datetime.today()
    today_month = today.month
    today_year = today.year
    total_days = 0
    if month:
        for x in range(month):
            if today_month != 13:
                monthrange = calendar.monthrange(today_year, today_month)[1]
                total_days += monthrange
                today_month += 1
            else:
                today_year += 1
                today_month = 1
    milliseconds = (total_days + weeks * 7 + day) * 86400
    time_stamp = time.time()
    return datetime.date.fromtimestamp(milliseconds + time_stamp)


if __name__ == '__main__':
    print(datetime.datetime.today())
    print(timing(2, 2, 12))
    delta = timing(2, 2, 12) - datetime.datetime.date(datetime.datetime.today())
    print(delta.days)
