# Crie um dicionario que guarde o nome, ano de nascimento, a idade
# o ano da contratação e o salário de um funcionário.
# Calcule e acrescente no dicionario quantos anos a pessoa se aposentará

Nome = input("Nome ")
Nascimento = int(input("Nascimento "))
Idade = 2023 - Nascimento
Contratação = int(input("Contratação "))
Salário = int(input("Salário "))

doc = {"Nome":Nome, "Nascimento":Nascimento, "Idade": Idade, "Contratação":Contratação, "Salário":Salário}

conTime = 2023 - Contratação
if conTime >= 15:
    if Idade < 65:
        Aposentadoria = 65 - Idade
    else:
        Aposentadoria = "Já se aposentou"
else:
    Aposentadoria = (15 - conTime) + (65 - Idade)

doc["Aposentadoria"] = Aposentadoria

print(doc)