# Classe "Círculo":
# Crie uma classe chamada "Círculo" que possua o método __init__
# para inicializar a propriedade "raio" do círculo.
# Em seguida, crie um objeto da classe "Círculo" e calcule e
# imprima a área do círculo.

class Circulo():
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return str(3.14 * (self.raio ** 2))


roda = Circulo(15)
print("A área é: " + Circulo.area(roda))
