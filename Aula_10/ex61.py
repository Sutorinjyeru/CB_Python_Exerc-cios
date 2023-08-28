# Dificuldade: Fácil

# Escreva um programa que peça ao usuário para digitar
# um número inteiro e, em seguida, imprima o dobro desse número.
# Utilizy try/except para lidar com a possibilidade de o
# usuário inserir um valor não numérico.


def main():
    num = int(input("Me vê o número aí colega "))
    print(dobro(num))

def dobro(x):
    while True:
        try:
            return x * 2
        except ValueError:
            print("Utilize somente números ")

main()