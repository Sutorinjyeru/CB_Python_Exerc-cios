# Crie um jogo que faça o computador pensar em um número de 0 a 5 e permita o usuario ter um chute pra acertar
import random

Right = random.randint(0,5)
num = int(input("Olá, escolha um número de 0 a 5\n"))

print(f"O número sorteado foi: {Right}")

if num == Right:
    print("Acertou! :D")
else:
    print("Errou! :(")