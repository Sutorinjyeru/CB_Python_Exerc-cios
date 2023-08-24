# Moderadamente difícil:
# Escreva uma função que recebe uma lista de strings como entrada e
# retorne um dicionário onde as chaves são as strings e os valores são os números

def dic():
    dicio = {}
    numeros = []
    letras = []
    text = str
    while text != ",":
        text = input()
        if text in "1234567890":
            numeros.append(text)
        else:
            letras.append(text)
    dicio = {**letras, **numeros}


dic()