# Ex08 - Diga se um valor numérico qualquer é par ou ímpar (Sem usar if)

num = int(input("Escolha o número:\n"))

print("O número é par" * (num % 2 == 0), "O número é ímpar" * (num % 2 != 0))
