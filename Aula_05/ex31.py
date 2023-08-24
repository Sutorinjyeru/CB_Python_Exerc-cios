# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou o tempo do alistamento.
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


# Pedindo input do usuário
year = int(input("Ano de nascimento\n"))

# Contas para saber a situação
age = (2023 - year)
time = (18 - age)
time2 = (time * (-1))

# Verificação
if age < 140:
    if year < 2020:
        if age < 18:
            print(f"Você ainda vai se alistar ao serviço militar daqui a {time} anos")
        elif age == 18:
            print("Esta é a hora exata de se alistar")
        else:
            print(f"Já passou da hora de se alistar\nVocê deveria ter se alistado há {time2} anos")
    elif year >= 2020 and year <2024:
        if year == 2023:
            print(f"Mal nasceu e já quer saber?\nFaltam {time} anos pro alistamento")
        else:
            print(f"Mal aprendeu a ler e já quer saber?\nFaltam {time} anos pro alistamento")
    elif year > 2023:
        print("E tu veio do futuro é? engraçadinho você hein")
else:
    print("Valeu ancião, mentiroso do caramba")