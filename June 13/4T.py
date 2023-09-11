class Chair:
    material = ''
    color = ''
    style = ''
    height = 0
    width = 0
    weight = 0
    price = 0

    def __init__(self, material, color, style, height, width, weight):
        self.material = material
        self.color = color
        self.style = style
        self.height = height
        self.width = width
        self.weight = weight

    def __repr__(self):
        message = '''
        This chair made of %s, color - %s, style - %s,
        height and width - %s, %s and weight - %s kg
        ''' % (self.material, self.color, self.style, self.height, self.width, self.weight)
        return message

    def get_price(self):
        price = (self.height * self.width) / 10
        self.price = price
        return 'Price of your chair - $%.2f' % price

    def is_comfy(self):
        if self.height > 40 and self.width > 40:
            return 'This chair is comfy.'
        else:
            return 'This chair is not comfy.'

    def repair(self):
        new_material = self.material
        return 'Chair has been repaired with %s!' % new_material

    def is_affordable(self):
        if self.price <= 100:
            return 'You can afford this chair.'
        else:
            return 'Too expensive bruh.'


my_chair = Chair('wood', 'brown', 'simple', 12, 53, 12)
print(my_chair)
print(my_chair.get_price())
print(my_chair.is_comfy())
print(my_chair.repair())
print(my_chair.is_affordable())