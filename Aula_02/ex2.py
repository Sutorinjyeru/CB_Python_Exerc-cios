""" faça um programa que leia a altura e a largura de uma parede e calcule
sua area, mostre quantos litros de tinta será necessário para
pintar sabendo que 1l pinta 2m quadrados """

alt = float(input("Qual a altura da parede?\n"))
larg = float(input("Qual a largura da parede?\n"))
tin = (alt * larg) / 2
print(f"Você precisa de {tin}l de tinta pra pintar a parede.")