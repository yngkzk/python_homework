from ticket import Ticket

class Kassa:
    balance = 0
    tickets = []
    registered_source = []
    registered_destination = []
    registered_train = []
    trains = []

    def register_train(self, source, destination=None):
        self.registered_source = [source]
        self.registered_destination = [destination]
        self.registered_train += zip(self.registered_source, self.registered_destination)
        return self.registered_train

    def get_price(self, source, destination):
        return (len(source) + len(destination)) * 1000

    def buy_ticket(self, source, destination, person):
        for i in self.registered_train:
            if i[0] == source and i[1] == destination:
                price = self.get_price(source, destination)
                money = person.pay(price)
                if money:
                    self.balance += money
                    new_ticket = Ticket(source, destination, person.name, person.iin, person.age)
                    self.tickets.append(new_ticket)
                    print("Номер вашего билета -", new_ticket.number)
                else:
                    print("No money - no ticket!")
            else:
                print("У нас нет такого поезда!")
                break

    def get_ticket(self, iin, source, destination):
        for x in self.tickets:
            if x.source == source and x.destination == destination and x.passenger_iin == iin:
                return x

    def delete_ticket(self, ticket):
        self.tickets.remove(ticket)


print("Это касса!", __name__)