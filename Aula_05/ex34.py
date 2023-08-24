# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

# Lendo as 3 retas
reta1 = int(input("Me informe a primeira reta\n"))
reta2 = int(input("Me informe a segunda reta\n"))
reta3 = int(input("Me informe a terceira reta\n"))

# Cálculos
if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta3 + reta1) > reta2:
    canBe = True
else:
    canBe = False
    print("Não tem como formar o triângulo")

if canBe == True:
    if reta1 == reta2 == reta3:
        print("EQUILÁTERO")
    elif reta1 != reta2 != reta3:
        print("ESCALENO")
    else:
        print("ISÓSCELES")