# leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# calcule e mostre o comprimento da hipotenusa
import math

ops = float(input("Cateto oposto\n"))
adj = float(input("Cateto Adjacente\n"))

hip = math.hypot(ops, adj)

print (f"A hipotenusa é: {hip}!")