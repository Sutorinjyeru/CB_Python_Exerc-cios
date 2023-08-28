# Moderado:
# Desenvolva uma função que verifique se uma palavra é um palíndromo
# (ou seja, lida da mesma forma da esquerda para a direita e vice-vesa).
# A função deve retornar True se a palavra for um palíndromo e
# False caso contrário

word = input("COE ")

def Palíndromo(x):
    if x == x[::-1]:
        return True
    else:
        return False
