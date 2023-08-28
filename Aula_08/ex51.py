# Crie um programa onde 4 jogadores jogam um dado
# Guarde esses resultados em um dicionario
# No final, coloque esse dicionario em ordem (1°, 2°...)
import random

p1 = random.randint(1,6)
p2 = random.randint(1,6)
p3 = random.randint(1,6)
p4 = random.randint(1,6)

great = 0
low = 0

tries = {"P1": p1, "P2": p2, "P3": p3, "P4": p4}

for i in sorted(tries, key = tries.get, reverse=True):
    print(i, tries[i])
