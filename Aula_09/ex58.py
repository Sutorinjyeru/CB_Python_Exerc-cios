# Moderadamente difícil:
# Crie uma função que receba um número inteiro como entrada e
# retorne uma lista de todos os divisores desse número.

num = int(input("aeaee "))

def DList(x):
    divis = []
    for i in range(1,x):
        if x % i == 0:
            divis.append(i)
    return divis
