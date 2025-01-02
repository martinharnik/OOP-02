class Type():
    def __init__(self, type):
        self.type = type

    def show_type(self):
        print(self.type)

class Color():
    def __init__(self, color):
        self.color = color

    def show_color(self):
        print(self.color)

class Animal(Type, Color):
    def __init__(self, type, color, eat):
        Type.__init__(self, type)
        Color.__init__(self, color)
        self.eat = eat

    def show_diet(self):
        print(self.eat)

animal = Animal("carnivore", "black", "meat")
animal.show_type()
animal.show_color()
animal.show_diet()