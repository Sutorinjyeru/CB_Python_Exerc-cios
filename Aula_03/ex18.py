# faça um programa que leia o nome de quatro alunos e escreva na tela o nome do escolhido para apagar o quadro

import random

nub1 = input("Primeiro aluno\n")
nub2 = input("Segundo aluno\n")
nub3 = input("Terceiro aluno\n")
nub4 = input("Quarto aluno\n")

chosen = random.choice([nub1, nub2, nub3, nub4])
print(f"{chosen} is the chosen one!")