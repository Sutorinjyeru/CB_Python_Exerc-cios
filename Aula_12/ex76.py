# Classe "Aluno":
# Crie uma classe chamada "Aluno" que possua o método __init__
# para inicializar as propriedades "nome" e "nota" do aluno.
# Em seguida, crie dois objetos da classe "Aluno" e verifique
# qual dos dois obteve a maior nota.

class Aluno():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def greater(x, y):
        print(f"O maior é: {x.nome}" * (x.nota > y.nota),
              f"O maior é: {y.nome}" * (y.nota > x.nota))


Carlos = Aluno("Carlos", 9)
Joestrela = Aluno("Joseph", 6)
Aluno.greater(Joestrela, Carlos)
