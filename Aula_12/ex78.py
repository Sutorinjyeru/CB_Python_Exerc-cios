# Classe "Pessoa":
# Crie uma classe chamada "Pessoa" que possua o método __init__
# para inicializar as propriedades "nome", "idade" e "profissão"
# da pessoa. Em seguida, crie um objeto da classe "Pessoa" e
# imprima todas as suas informações

class Pessoa():
    def __init__(self, nome, idade, profissão):
        self.nome = nome
        self.idade = idade
        self.profissão = profissão

    def infos(self):
        print(
            f"Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissão}")


josé = Pessoa("José", "27", "Jornalista")
josé.infos()
