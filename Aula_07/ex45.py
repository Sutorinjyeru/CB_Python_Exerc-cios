# Melhore o jogo de adivinhação onde o computador "pensa"
# em um número. Mostre quantos palpites o usuário usou


# import
import random

# Variáveis
pal = 0
hit = False

# Jogo
while hit == False:
    right = random.randint(0,5)
    num = int(input("Pegue um número\n"))
    pal = pal + 1
    if num == right:
        hit = True
        print(f"Você ganhou com {pal} tentativas")
    else:
        print("Errou")

