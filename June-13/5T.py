import time


class Timer:
    start_time = 0
    end_time = 0
    duration = 0
    is_running = None
    delay = 0
    interval = 1

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = 0
        self.is_running = False
        self.delay = 0

    def set_delay(self, delay):
        self.delay = delay
        time.sleep(self.delay)
        return 'Delay set to - %s' % self.delay

    def set_interval(self, interval):
        self.interval = interval
        return 'Interval set to - %s' % self.interval

    def start_timer(self):
        self.start_time = time.time()
        self.is_running = True
        return 'Time started running.'

    def stop_timer(self):
        time.sleep(self.delay)
        self.end_time = time.time()
        self.is_running = False
        self.duration = self.end_time - self.start_time + self.delay
        return 'Time stopped.'

    def reminder(self):
        local_time = self * 60
        time.sleep(local_time)
        return 'You have to do something!'


my_timer = Timer(1, 2)
print(my_timer.set_delay(2))
print(my_timer.set_interval(1))
print(my_timer.start_timer())
print(my_timer.stop_timer())
print(Timer.reminder(1))
