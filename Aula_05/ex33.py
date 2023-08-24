# A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

# Lendo o ano de nascimento do atleta
year = int(input("ANO:\n"))

# Conta da idade
age = (2023 - year)

# Verificando a situação do atleta
if age <= 25:
    print(f"you may be an athlete but we do not grant you the rank of master")
    if age <= 9:
        print("MIRIM")
    elif age <= 14:
        print("INFANTIL")
    elif age <= 19:
        print("JÛNIOR")
    else:
        print("SENIOR")
elif age >150:
    print("VALEU ANCIÃO")
else:
    print("MASTER")