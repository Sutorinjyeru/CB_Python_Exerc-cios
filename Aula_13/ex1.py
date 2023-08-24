# Classe "Cachorro":
# Crie uma classe chamada "Cachorro" que possua o método
# __init__ para inicializar as propriedades "nome" e "idade"
# do cachorro. Em seguida, crie um objeto da classe "Cachorro"
# e imprima o nome do cachorro.

class Cachorro():
    def __init__(self, nome, age):
        self.nome = nome
        self.idade = age

def main():
    puppie = Cachorro("Spike", 13)
    print(puppie.nome)

main()