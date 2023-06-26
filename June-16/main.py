from hotel import Hotel
from person import Person
from room import Room


test = Person('Человек', 21)
test.earn(97000)
test.pay(7000)
test.show()

rixos = Hotel('Rixos')
price = rixos.get_price(1, 2, 5)
test_pass = rixos.buy_order(1, 2, 5, test)

room = Room()
check = room.is_empty(3)

