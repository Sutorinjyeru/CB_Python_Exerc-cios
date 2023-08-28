# Crie um programa que leia o numero de um usuario e mostre sua tabuada(de 1 até 50)

num = int(input("Passe o número desejado\n:"))
tabuada = 0

print(f"A tabuada de {num} é:")
for i in range(1,11):
    tabuada = num * i
    print(f"{num} * {i} = {tabuada}")