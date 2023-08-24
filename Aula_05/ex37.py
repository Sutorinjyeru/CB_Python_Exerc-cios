# Faça o jogo pedra papel e tesoura

import random

#p1
mode = int(input("Vs CPU ou Vs P2?(1=CPU/2=P2)\n"))
choice = input("Player 1: Pedra, Papel, Tesoura(1=pedra/2=papel/3=tesoura)\n")
rock = "Pedra"
paper = "Papel"
scissor = "Tesoura"

# CPU
if mode == 1:
    choice1 = random.randint(1,3)
    p2 = "CPU"
elif mode == 2:
    choice1 = int(input("Player 2: Pedra, Papel, Tesoura(1=pedra/2=papel/3=tesoura)\n"))
    p2 = "P2"

# Player choice
if choice == "1":
    choice = rock
elif choice == "2":
    choice = paper
elif choice == "3":
    choice = scissor
else:
    print("Tem que escolher entre 1, 2 ou 3")

if choice1 == 1:
    textC = "Pedra"
elif choice1 == 2:
    textC = "Papel"
elif choice1 == 3:
    textC = "Tesoura"


# Match result
if choice == rock:
    if choice1 == 1:
        win = "Empatou"
    elif choice1 == 2:
        win = "Perdeu"
    elif choice1 == 3:
        win = "Ganhou"
elif choice == paper:
    if choice1 == 1:
        win = "Ganhou"
    elif choice1 == 2:
        win = "Empatou"
    elif choice1 == 3:
        win = "Perdeu"
elif choice == scissor:
    if choice1 == 1:
        win = "Perdeu"
    elif choice1 == 2:
        win = "Ganhou"
    elif choice1 == 3:
        win = "Empatou"

print(f"P1 escolheu {choice} e o {p2} {textC}.")
print(f"P1 {win}")