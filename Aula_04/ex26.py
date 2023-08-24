"""Escreva um código que pergunte o salário de um funcionario e de um aumento de
15% caso o salário for maior que 1250 reais, caso contrário 10%"""

wage = float(input("Me informe o salário\n"))
if wage > 1250:
    incr = 0.15 * wage
else:
    incr = 0.10 * wage
result = (wage + incr)

print(f"O aumento é de {incr} resultado é {result}!")