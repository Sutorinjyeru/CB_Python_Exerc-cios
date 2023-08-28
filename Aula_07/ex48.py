# Refaça o desafio do PA mostrando os 20 primeiros termos
# e pergunte ao usuário quantos termos a mais ele quer ver
# o programa encerra quando disser que quer mostrar os 0 termos


ask = int

def PA(x,y, z=0):
    for i in range(1, 21+z):
        p = x + (i-1) * y
        print(i, p)

while True:
    term = int(input("Termo "))
    reas = int(input("Razão "))
    PA(term, reas)
    ask = int(input("Quantos termos a mais o sinhô qué?\n"))
    if ask != 0:
        PA(term, reas, ask)
    else:
        break