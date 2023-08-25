# Crie um programa para um sistema de reservas de quartos
# de hotel, onde as chaves são os números dos quartos
# e os valores são booleanos para indicar se o quarto está
# disponível(True) ou ocupado(False). O programa deve permitir
# que o usuário consulte a disponibilidade de
# quartos, reserve um quarto específico e cancele uma reserva
# Ao realizar uma reserva, o estado do quarto deve ser atualizado no dicionário.

from random import choice

rooms = {}

for i in range(10):
    rooms["Quarto " + str(i)] = choice([True, False])


def main():

    print_rooms()
    while True:
        x = input("Escolha o número do quarto desejado:\n")
        rooms["Quarto " + x]
        if rooms["Quarto " + x] == True:
            rooms["Quarto " + x] = False
            if input(f"{rooms} gostaria de cancelar a reserva?(1=Sim. 2=Não)\n") != "1":
                rooms["Quarto " + x] = True
                print_rooms()
            else:
                print("Muito obrigado. Volte sempre. ")
                break
        elif ["Quarto " + x] == False:
            if input("Quarto indisponível, gostaria de reservar outro?(1=Sim. 2=Não)\n") != "1":
                print("Tudo bem. Volte sempre! ")
                break


def print_rooms():
    print(f"Disponibilidade dos quartos: {rooms}")


main()
