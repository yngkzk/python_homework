from hotel import Hotel
from person import Person
from room import Room


test = Person('Human', 21)
test.earn(97000)
test.pay(7000)
test.show()

rixos = Hotel('Rixos')
print(rixos.get_price(1, 2, 5))
print(Room.is_empty(3))
print(rixos.buy_order(1, 2, 5, test))

print(rixos.check_in(test, 3))
print(Room.is_empty(3))
print(rixos.check_out(test, 6))