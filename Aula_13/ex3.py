# Classe "Aluno":
# Crie uma classe chamada "Aluno" que possua o método __init__
# para inicializar as propriedades "nome" e "nota" do aluno.
# Em seguida, crie dois objetos da classe "Aluno" e verifique
# qual dos dois obteve a maior nota.

class Aluno():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


def maior(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    Carlos = Aluno("Carlos", 9)
    #Joestrela = Aluno("Joseph", 7)
    print(type (Carlos))

main()