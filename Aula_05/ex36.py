# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

import math

# Leitura blablabla
price = float(input("Qual o preço do produto?\n"))
Pmethod = input("Qual o método de pagamento?(1=dinheiro/2=cheque/3=cartão)\n")
value = 0.0

if Pmethod == "2":
    print(f"Para {Pmethod} a única opção é pagar à vista.")
    value = price - (price / 10)
    print("10% desconto")
elif Pmethod == "3":
    condition = input("Qual método deseja escolher?(v=à vista, p= parcelado)")
    if condition == "v":
        value = price - (price / 20)
        print("5% desconto")
    elif condition == "p":
        inst = int(input("Quer parcelar em quantas vezes?"))
        if inst == 2:
            value = price
        elif inst <= 3:
            fees = price + (price / 5)
            prov = price / (1-(1+ fees) ** (inst * (-1))/ fees)
            value = price + prov
            print (f"installments:{inst}, fees:{fees}, provisions{prov}")
else:
    print("Não foi possível verificar o método de pagamento, tente novamente.")
print(f"O valor do pagamento é {value}")