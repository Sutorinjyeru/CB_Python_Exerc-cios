# Crie um programa que leia idade e sexo de varias pessoas.
# Depois, mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos



def count():
    read = ""
    a = 0
    b = 0
    c = 0
    while read != "0":
        genre = input("gen ")
        age = int(input("age "))
        read = input("AEE ")
        if age > 18:
            a += 1
        if genre == "M":
            b +=1
        if genre == "W":
            if age < 20:
                c +=1
    print(a, b, c)

count()