""" Fala um programa que leia a distancia em km de uma viagem, se a distância for menor ou igual a 200km
cobre 50 centavos por km rodado, caso contrário cobre 45 centavos."""

dist = int(input("Qual a distância da viagem?(km)\n"))

if dist <= 200:
    print(f"A distância é {dist}, a conta deu 50 centavos.")
else:
    print(f"A distância é {dist}, a conta deu 45 centavos.")