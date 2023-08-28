# Moderado:
# Escreva uma função que receba uma lista de palavras como entrada
# e retorne uma lista apenas com as palavras que têm mais de 5 letras.

Words = []
z = int(input("Tamanho da lista"))

def BWords(x,z=5):
    for i in range(z):
        value = input("Bruh ")
        if len(value) > 5:
            Words.append(value)
    return x

print(BWords(Words,z))