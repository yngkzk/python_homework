class Animal:
    name = ''
    weight = 0
    size = 0

    def __init__(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size

    def __repr__(self):
        info = 'Animal name: %s, weight and size: %dkg & %dm' % (self.name, self.weight, self.size)
        return info

    def talk(self):
        message = 'Mmmmm...'
        return message

    def eat(self, meal):
        resources = len(meal)
        self.size += resources
        self.weight += resources
        message = 'Now your weight and size, %dkg and %dm' % (self.weight, self.size)
        return message


class Herbivore(Animal):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size)
    # VN: если вы в конструкторе ничего нового не делаете, то можете его вообще не писать - будет автоматически
    # вызываться конструктор родительского класса

    def __repr__(self):
        info = 'Herbivore name: %s, weight and size: %dkg & %dm' % (self.name, self.weight, self.size)
        return info

    def talk(self):
        return super().talk()
    # VN: то же самое и с методами - не нужно их переопределять, если они должны работать так же, как и родительские

    def eat(self, food):
        ratio = ['leaf', 'grass', 'plants']
        # VN:   ^^^^^^^^^^^^^^^^^^^^^^^^^^^ по условию задачи этот список должен быть в конструкторе,
        # и передаваться в него в качестве аргумента
        if food in ratio:
            return super().eat(food)
        return 'You can not eat this'


class Predator(Animal):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size)

    def __repr__(self):
        info = 'Predator name: %s, weight and size: %dkg & %dm' % (self.name, self.weight, self.size)
        return info

    def talk(self):
        return super().talk()
    # VN: ну вы поняли) Хотя для хищников можно сделать "Rrrrrr!"

    def eat(self, animal):
        # VN: Тут нужна проверка isinstance, чтобы убедиться, что animal здесь действительно является
        # экземпляром класса Animal. Иначе попытка обратиться к animal.weight приведёт к падению
        if animal.weight < self.weight:
            self.weight += animal.weight * 0.2
            if animal.size < self.size:
                self.size += animal.size * 0.2
                return 'Now your weight and size, %dkg and %dm' % (self.weight, self.size)
        return 'You can not eat this'


class Goose(Herbivore):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size)
    # VN: нет смысла в переопределении этого конструктора

    def __repr__(self):
        info = 'Goose name: %s, weight and size: %dkg & %dm' % (self.name, self.weight, self.size)
        return info

    def talk(self):
        return 'Ga-ga-ga'

    def eat(self, food):
        return super().eat(food)
    # VN: нет смысла в переопределении этого метода


class Wolf(Predator):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size)
    # VN: нет смысла в переопределении этого конструктора

    def __repr__(self):
        info = 'Wolf name: %s, weight and size: %dkg & %dm' % (self.name, self.weight, self.size)
        return info

    def talk(self):
        return 'Wooooo!!!'

    def eat(self, animal):
        return super().eat(animal)
    # VN: нет смысла в переопределении этого метода


my_animal = Animal('Wolf', 24, 7)
print(my_animal)
print(my_animal.talk())
print(my_animal.eat('Food'))

my_herbivore = Herbivore('Cow', 54, 34)
print(my_herbivore)
print(my_herbivore.talk())
print(my_herbivore.eat('leaf'))

my_predator = Predator('Python enjoyer', 75, 52)
print(my_predator)
print(my_predator.talk())
print(my_predator.eat(my_herbivore))

my_goose = Goose('Goose goose duck', 12, 5)
print(my_goose)
print(my_goose.talk())
print(my_goose.eat('plants'))

my_wolf = Wolf('Qasqyr', 32, 21)
print(my_wolf)
print(my_wolf.talk())
print(my_wolf.eat(my_goose))

# VN: если создать много волков, то они смогут есть по почереди одного и того же гуся. Исправьте это
