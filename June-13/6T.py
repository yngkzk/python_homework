class Car:
    make = ''
    model = ''
    year = 0
    color = ''
    mileage = 0
    price = 0

    def __init__(self, make, model, year, color, mileage, price):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.price = price

    def __repr__(self):
        message = '''
        Make - %s
        Model - %s
        Year - %s
        Color - %s
        Mileage - %s miles
        Price - $%s
        ''' % (self.make, self.model, self.year, self.color, self.mileage, self.price)
        return message

    def start(self):
        message = "The %s %s has started." % (self.make, self.model)
        return message

    def stop(self):
        message = "The %s %s has stopped." % (self.make, self.model)
        return message

    def drive(self, distance):
        self.mileage += distance
        message = "The %s %s has been driven for %s miles." % (self.make, self.model,
                                                               distance)
        return message


my_car = Car('Toyota', 'Camry', 2022, 'Silver', 5000, 25000)

print(my_car)
print(my_car.start())
print(my_car.drive(200))
print(my_car.stop())
