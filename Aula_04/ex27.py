# Faça um programa que leia as 3 retas do usuario e diga se elas podem formar um triângulo

reta1 = input("Me informe a primeira reta\n")
reta2 = input("Me informe a segunda reta\n")
reta3 = input("Me informe a terceira reta\n")

#
if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta3 + reta1) > reta2:
    print("Elas podem formar um triângulo.")
else:
    print("Elas não podem formar um triângulo.")