# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# Calcule seu índice de Massa Corporal (IMC) e mostre seu status,
# De acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

# Lendo peso e altura
weight = float(input("Peso(kg)\n"))
height = float(input("Altura(m)\n"))

# Cálculo do IMC
imc = weight / (height ** 2)

print(f"o imc é {imc}")
# Verificação de status
if imc < 18.5:
    print("Abaixo do Peso")
elif imc <= 25:
    print("Peso ideal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")