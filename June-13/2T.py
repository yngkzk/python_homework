class Pencil:
    model = ''
    series = ''
    color = ''
    weight = 0
    shape = ''
    size = 0
    text = ''

    def __init__(self, model, series, color, weight, shape, size):
        self.model = model
        self.series = series
        self.color = color
        self.weight = weight
        self.shape = shape
        self.size = size

    def __repr__(self):
        message = "Model & series - %s, %s, color - %s, weight - %sg, shape - %s, size - %s" % (self.model, self.series,
                                                                                                self.color, self.weight,
                                                                                                self.shape, self.size)
        return message

    def write(self, note):
        self.text += note
        return "Text - %s" % self.text

    def draw(self, note):
        self.text = ''
        self.text += note
        return "You drew %s with %s color!" % (self.text, self.color)

    def highlight(self, note):
        self.text = ''
        self.text += note
        return " [ " + self.text + " ] "

    def paint_over(self, cells):
        self.text = '#'
        self.text *= cells
        return "You painted over " + self.text + " this."


my_pencil = Pencil("Simple", "TypeSimple", "red", 42, "triangle", 12)
print(my_pencil)
print(my_pencil.write("Example for text"))
print(my_pencil.draw("Elephant"))
print(my_pencil.highlight("Important text"))
print(my_pencil.paint_over(12))
