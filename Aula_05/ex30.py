# Escreva um programa que leia dois números inteiros e compare-os
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

# Pegando input do usuário
num1 = int(input("Primeiro número.\n"))
num2 = int(input("Segundo número.\n"))
# Lógica e resultado
if num1 > num2:
    print("O primeiro valor é maior.")
elif num1 < num2:
    print("O o segundo valor é maior.")
elif num1 == num2:
    print("Não existe valor maior, os dois são iguais.")
else:
    print("Inválido")