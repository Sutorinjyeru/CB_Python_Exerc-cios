"""Faça um programa que leia a quantidade de dias e km rodados por um carro
alugado, depois calcule o valor do contrato sabendo que:
cada dia custa 60 reais e cada km custa 15 centavos"""

days = int(input("Quantos dias?"))
km = int(input("Quantos kms?"))
cost = (60 * days) + (15 * km)
print(f"O valor do contrato é:{cost}!")
