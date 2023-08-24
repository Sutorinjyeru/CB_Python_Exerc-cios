# Crie um programa que simule uma corrida entre dois carros,
# onde os carros avançam a cada iteração do loop. O carro A
# e carro B começam na posição 0. Cada carro avança uma
# distância aleatória entre 1 e 5. O carro que atingir
# a posição de 30 primeiro é declarado vencedor.

import random

car1 = 0
car2 = 0
winner = 0

while winner == 0:
    car1 += random.randint(1,5)
    car2 += random.randint(1,5)
    print(car1, car2)
    if car1 >= 30:
        winner = car1
        print(f"Carro 1 venceu")
    if car2 >= 30:
        winner = car2
        print(f"Carro 2 venceu")