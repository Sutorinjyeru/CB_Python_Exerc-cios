# Escreva um programa em python que que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

# Pedindo input do usuário
base = input("Base(1,2,3)\n")

num = int(input("Número\n"))

# Lógica da base escolhida
if base == "1":
    print(f'{num:b}')
elif base == "2":
    print(f"{num:o}")
elif base == "3":
    print(f"{num:e}")
else:
    print("Invalid")