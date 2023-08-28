class Animal:
    name = ''
    weight = 0
    size = 0

    def __init__(self, name, weight, size, ratio=None):
        self.name = name
        self.weight = weight
        self.size = size
        self.ratio = ratio

    def __repr__(self):
        info = 'Animal name: %s, weight and size: %dkg & %dm' % (self.name, self.weight, self.size)
        return info

    def talk(self):
        message = 'Mmmmm...'
        return message

    def eat(self, meal):
        resources = len(meal) // 3
        self.size += resources
        self.weight += resources
        message = 'Now your weight and size, %dkg and %dm' % (self.weight, self.size)
        return message


class Herbivore(Animal):

    def __init__(self, name, weight, size, ratio):
        super().__init__(name, weight, size, ratio)

    def __repr__(self):
        info = 'Herbivore name: %s, weight and size: %dkg & %dm' % (self.name, self.weight, self.size)
        return info

    def eat(self, food):
        if self.ratio:
            if food in self.ratio:
                return super().eat(food)
        return 'You can not eat this or its nothing'


class Predator(Animal):

    def __repr__(self):
        info = 'Predator name: %s, weight and size: %dkg & %dm' % (self.name, self.weight, self.size)
        return info

    def talk(self):
        return '*Angry & scary sounds*'

    def eat(self, animal):
        if isinstance(animal, Animal):
            if animal.weight:
                if animal.weight < self.weight:
                    self.weight += animal.weight * 0.2
                    if animal.size < self.size:
                        self.size += animal.size * 0.2
                    del animal.weight
                    return 'Now your weight and size, %dkg and %dm' % (self.weight, self.size)
        return 'You can not eat this or its nothing'


class Goose(Herbivore):
    
    def __repr__(self):
        info = 'Goose name: %s, weight and size: %dkg & %dm' % (self.name, self.weight, self.size)
        return info

    def talk(self):
        return 'Ga-ga-ga'


class Wolf(Predator):

    def __repr__(self):
        info = 'Wolf name: %s, weight and size: %dkg & %dm' % (self.name, self.weight, self.size)
        return info

    def talk(self):
        return 'Wooooo!!!'


my_animal = Animal('Wolf', 24, 7)
print(my_animal)
print(my_animal.talk())
print(my_animal.eat('Food'))
print('\n')

my_herbivore = Herbivore('Cow', 54, 34, ['leaf', 'plants', 'grass'])
print(my_herbivore)
print(my_herbivore.talk())
print(my_herbivore.eat('leaf'))
print('\n')

my_predator = Predator('Python enjoyer', 75, 52)
print(my_predator)
print(my_predator.talk())
print(my_predator.eat(my_herbivore))
print('\n')

my_predator = Predator('Python enjoyer', 75, 52)
print(my_predator)
print(my_predator.talk())
print(my_predator.eat(my_herbivore))
print('\n')

my_goose = Goose('Goose goose duck', 12, 5, ['leaf', 'something but not plants :C'])
print(my_goose)
print(my_goose.talk())
print(my_goose.eat('plants'))
print('\n')

my_wolf = Wolf('Qasqyr', 32, 21)
print(my_wolf)
print(my_wolf.talk())
print(my_wolf.eat(my_goose))
print('\n')
