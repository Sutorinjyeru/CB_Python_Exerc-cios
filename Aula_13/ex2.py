# Classe "Retângulo":
# Crie uma classe chamada "Retângulo" que possua o método
# __init__ para inicializar as propriedades "largura" e "altura"
# do retângulo. Em seguida, crie um objeto da classe "Retângulo"
# e calcule e imprima a área do retângulo.


class Retângulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


def área(Larg, Alt):
    return Larg * Alt


def main():
    retângulo = Retângulo(20, 20)
    print(área(retângulo.largura, retângulo.largura))

main()