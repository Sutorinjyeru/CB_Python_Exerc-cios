# Desenvolva um programa que calcule a soma de todos números
# Múltiplos de três entre 1 e 500
# E mostre quantos numeros são divisiveis

soma = 0

for item in range(1,500):
    if item % 3 == 0:
        soma = soma + item
        print(item)
print(soma)