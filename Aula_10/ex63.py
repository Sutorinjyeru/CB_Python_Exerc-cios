# Escreva um programa que solicite ao usuário que digite seu
# nome e sua idade. Em seguida, tente converter a idade em
# um número inteiro. Se a conversão falhar,
# informe ao usuário que a idade digitada é inválida e
# continue o programa.
# Caso contrário, exiba uma mensagem com o nome e a idade.


def main():
    num1 = input("Nome: ")
    num2 = input("Idade: ")
    check(num1,num2)
    

def check(x,y):
    try:
        int(y)
    except ValueError:
        print("KOE DA NUMERO CARA...")
    else:
        print(f"O nome é {x} e a idade é {y}")

main()