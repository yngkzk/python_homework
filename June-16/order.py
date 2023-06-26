from random import randint


class Order:
    hotel_name = ''
    id = 0  # random
    room = 0
    date_from = 0
    date_to = 0
    visitor_name = ''
    visitor_iin = 0

    def __init__(self, hotel_name, room, date_from, date_to, visitor_name, visitor_iin):
        self.hotel_name = hotel_name
        self.id = randint(1, 100)
        self.room = room
        self.date_from = date_from
        self.date_to = date_to
        self.visitor_name = visitor_name
        self.visitor_iin = visitor_iin

    def __repr__(self):
        message = 'Your room and id - %s, %s.' % (self.room, self.id)
        return message

    def show_info(self):
        message = 'Dear %s, welcome to %s, your room and id - %s, %s.' % (self.visitor_name, self.hotel_name,
                                                                          self.room, self.id)
        message += 'INFO: date from - %s, to - %s. IIN: %s' % (self.date_from, self.date_to, self.visitor_iin)
        return message
