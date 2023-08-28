# Crie uma função chamada "divide_numbers" que recebe dois parâmetros
# numéricos (a e b) e retorna a divisão de a por b.
# Utilize try/except para tratar a divisão por zero.


def main():
    num1 = int(input("AA "))
    num2 = int(input("OOO "))
    print(divide_numbers(num1,num2))

def divide_numbers(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Você tentou dividir por zero")
        return a

main()