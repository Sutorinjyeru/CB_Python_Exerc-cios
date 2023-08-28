# Dificuldade: Intermediária

# Escreva um programa que leia um valor numérico inteiro
# do usuário e imprima o resultado da raiz quadrada desse
# valor. Utilize try/except para lidar com a possibilidade
# de o usuário inserir um número negativo.

from math import sqrt

num1 = int(input("aeee"))


try:
    sqrt(num1)
except ValueError:
    print("Don't use negative numbers. ")
else:
    print(sqrt(num1))
