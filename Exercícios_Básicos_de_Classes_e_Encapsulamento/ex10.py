# Crie uma classe Shape com um método abstrato calculate_area.
# Em seguida, defina classes derivadas Circle e Triangle que herdam de Shape e
# implementam esse método para calcular suas respectivas áreas.

class Shape:
    def __init__(self, val, value):
        self.val = val
        self.value = value

    def calculate_area():
        pass


class Circle(Shape):
    def __init__(self, val, value):
        super().__init__(val, value)

    # def calculate_area(raio):
        # return 3.14 * (raio **2)


class Triangle(Shape):
    def __init__(self):
        super().__init__()

    # def calculate_area(base, altura):
        # return (base * altura) / 2
