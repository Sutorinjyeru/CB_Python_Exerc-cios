#Faça um programa que leia a quilometragem de um carro, caso esteja acima dos 80km/h, multe o carro

km = float(input("Mim ve a quilometragem\n"))

if km > 80:
    print("O carro foi multado.")
else:
    print("O carro não foi multado.")