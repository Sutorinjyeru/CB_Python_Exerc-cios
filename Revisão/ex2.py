# Crie um programa que receba o nome e as notas de 3
# disciplinas de um aluno. Armazene essas informações
# em um dicionário onde a chave é o nome da disciplina
# e o valor é a sua nota. No final, calcule a média das notas
# e exiba o nome do aluno, as disciplinas com suas respectivas
# notas e a média calculada

dicio = {}

student = input("Aluno:\n")

def main():
    average_ = 0
    for _ in range(3):    
        discipline = input("Disciplina:\n")
        note = int(input("Nota:\n"))
        average_ += note
        dicio[discipline] = note

def average(x,y):
    return x/y

def result():
    print(f"Aluno:{student}, disciplinas:{dicio}, média: {média}")
    print(dicio)

main()