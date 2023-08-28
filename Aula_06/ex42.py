# Leia o primeiro termo e a razão de uma PA. Depois, mostre
# os 20 primeiros termos.

term = int(input("Termo "))
reas = int(input("Razão "))


for i in range(term-reas,21):
    PA = term + (i-1) * reas
    print(PA)