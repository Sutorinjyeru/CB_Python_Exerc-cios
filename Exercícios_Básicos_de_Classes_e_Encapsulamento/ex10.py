# Crie uma classe Shape com um método abstrato calculate_area.
# Em seguida, defina classes derivadas Circle e Triangle que herdam de Shape e
# implementam esse método para calcular suas respectivas áreas.

class Shape:
    def __init__(self, form):
        self.form = form

    def calculate_area(self, y=1):
        if isinstance(self, Circle):
            return 3.14 * (self.form **2)
        elif isinstance(self, Triangle):
            return (self.form * y) / 2

class Circle(Shape):
    def __init__(self, form):
        super().__init__(form)

class Triangle(Shape):
    def __init__(self, form):
        super().__init__(form)


def main():
    triangulosan = Triangle(30)
    circlesan = Circle(32)

    print(triangulosan.calculate_area(44))
    print(circlesan.calculate_area(44))

if __name__ == "__main__":
    main()