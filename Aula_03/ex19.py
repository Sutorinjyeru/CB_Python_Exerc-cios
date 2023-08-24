# agora, sorteie uma ordem aleatória de 4 alunos. leia o nome dos alunos e mostre a ordem aleatória

import random

nub1 = input("Primeiro aluno\n")
nub2 = input("Segundo aluno\n")
nub3 = input("Terceiro aluno\n")
nub4 = input("Quarto aluno\n")

order = random.deck = f"{nub1}, {nub2}, {nub3}, {nub4}".split()
random.shuffle(random.deck)
print(f"{order} is the order.")