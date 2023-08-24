# Desenvolva uma mini calculadora em que seja permitido:
# somar, multiplicar, maior(mostrar o maior valor dentre os dois),
# novos numeros(escolher dois novos números) e sair do programa.

# Lista e variável

oprl = ["1= Soma, 2= Multiplicação, 3 = Maior, 4 = Sair"]
num1 = 0
num2 = 0

# Funç

def soma(x, y):
    z = x + y
    print(f"A soma de {x} + {y} é igual a {z}!")

def multi(x, y):
    z = x * y
    print(f"A multiplicação de {x} x {y} é igual a {z}!")

def maior(x,y):
    if x > y:
        print(f"O maior dentre {x} e {y} é {x}!")
    elif x < y:
        print(f"O maior dentre {x} e {y} é {y}!")
    elif x == y:
        print(f"Os números {x} e {y} são iguais.")

# Programa

while True:
    UsOpr = input(f"Escolha o que tu quer da vida{oprl}\n")
    if UsOpr == "1":
        num1 = int(input("Num1"))

        num2 = int(input("Num2"))

        soma(num1, num2)
    elif UsOpr == "2":
        num1 = int(input("Num1"))

        num2 = int(input("Num2"))

        multi(num1, num2)
    elif UsOpr == "3":
        num1 = int(input("Num1"))

        num2 = int(input("Num2"))

        maior(num1, num2)
    else:
        break
