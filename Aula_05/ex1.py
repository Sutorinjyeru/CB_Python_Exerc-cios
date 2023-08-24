# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou o empréstimo será negado.

# Pegar valor da casa, salario e quantos anos
value = float(input("Valor da casa\n"))
sal = float(input("Salário\n"))
years = float(input("Anos\n"))

# Lógica da prestação
prest = (value/ years) / 12

# Isso é só pra ver a prestação, será apagado
print(f"a prestação mensal é: {prest}\n")

# Ver se o empréstimo será aceito ou negado.
if prest <= (sal *0.3):
    print("Empréstimo aceito.")
else:
    print("Empréstimo negado.")