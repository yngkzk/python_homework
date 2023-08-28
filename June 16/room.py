from order import Order


class Room:
    number = 0
    bedrooms = 0
    order = None

    def is_empty(self, date=None):
        if date == Order.date_from:
            # VN:  ^^^^^ здесь обращение не к экземпляру, а к самому классу, т.е. просто к шаблону. Ошибка
            message = 'No suitable rooms for this day'
            return message
        else:
            return True

    def show_info(self):
        if self.number % 2 == 0:
            message = "Number of bedrooms: 2"
        else:
            message = "Number of bedrooms: 1"
        message += 'Welcome, your room N%s' % self.number
        return message
        self.number += 1
