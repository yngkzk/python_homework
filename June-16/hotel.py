from room import Room
from order import Order


class Hotel:
    name = ''
    balance = 0
    date_from = 0
    date_to = 0
    order = None

    def __init__(self, name):
        self.name = name

    def get_price(self, room_number, date_from, date_to):
        message = (date_from + date_to) * 1000 + (room_number * 100)
        return message

    def buy_order(self, room_number, date_from, date_to, visitor):
        price = self.get_price(room_number, date_from, date_to)
        money = visitor.pay(price)
        if money:
            self.balance += money
            message = 'You have booked a room!'
            message += '  Room N%s, from %s - to %s, visitor: %s' % (room_number, date_from, date_to, visitor.name)
            return message
        else:
            return 'You have not enough money!'

    def check_in(self, visitor, date):
        if visitor.iin == Order.visitor_iin:
            message = 'Welcome %s, your room N%s. To date %s.' % (visitor, Room.number, date)
            print(message)
            Room.show_info(self)
        else:
            print("You don't have pass")

    def check_out(self, visitor, date):
        if date > self.date_from - self.date_to:
            date_payment = (self.date_to + date) * 1000
            return '%s, you have to pay $%s' % (visitor, date_payment)
        else:
            price = self.get_price
            return '%s, you have to pay $%s' % (visitor, price)
