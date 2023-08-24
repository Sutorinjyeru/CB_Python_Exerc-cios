# Gerencie um jogador de futebol lendo o nome e quantas partidas ele jogou
# Depois, leia a quantidade de gols feitas em cada partida
# Coloque tudo num dicionário incluindo o total de gols durante o período

doc = {}

doc["Nome"] = input("Nome: ")

x = int(input("Partidas: "))

doc["Partidas"] = x

y = int(input("Gols: "))

doc["Gols"] = y

doc["Gols totais"] = x * y

print(doc)