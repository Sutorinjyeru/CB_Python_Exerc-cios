# leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

import math

num = float(input("Me vê o ângulo\n"))
cos = math.cos(num)
sin = math.sin(num)
tan = math.tan(num)
print(f"Seno={sin}, Cosseno={cos}, Tangente={tan}")