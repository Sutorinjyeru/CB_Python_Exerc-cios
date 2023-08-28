# crie um conversor de temperatura(C° F° K)
cel = float(input("INFORME EM GRAUS CELSIUS"))
far = ((cel * 9)/5) + 32
kel = (cel + 273.15)
print(f"{far} F° {kel} K")

farTemp = float(input("INFORME EM FARENHEIT"))
farKel = (farTemp - 32) * 5/9 + 273.15
farCel = (farTemp - 32) * 5/9
print(f"{farKel} K {farCel} C°")

kelTemp = float(input("INFORME EM KELVIN"))
kelFar = (((kelTemp - 273.15) * 9) / 5) + 32
kelCel = (kelTemp - 273.15)
print(f"{kelFar} F° {kelCel} C°")
