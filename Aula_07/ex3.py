# Mostre o fatorial de um numero enviado pelo usuario
# ex: 5x4x3x2x1 = 120

# Variável
cont1 = True

# Funç
def fatorial(x):
    f = 1
    for i in range(x, 1, -1):
        f = f * i
    return f

# Programa
while cont1 == True:
    num = int(input("Escolha um número"))

    fatorial(num)

    print(f"O fatorial de {num} é: {fatorial(num)}!")
    cont = input("Deseja continuar? Se sim, pressione 1, se não aperte qualquer botão.")

    if cont == "1":
        cont1 = True
    else:
        cont1 = False