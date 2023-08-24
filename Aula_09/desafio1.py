# Desafio 1:
# Agora faça o exercício acima aceitar vários jogadores, inclua um sistema
# para vizualizar detalhes do aproveitamento de cada jogador

# Lista pro número de jogadores
jogadores = []

PNum = int(input("Quantos jogadores?: "))

for i in range(PNum):
    jogadores.append(input("Nome(s): "))

def Jogador(F):
    l = {}
    l["Nome"] = F
    x = int(input("Partidas: "))
    l["Partidas"] = x
    y = int(input("Gols: "))
    l["Gols"] = y
    l["Gols totais"] = x * y
    return l

for i in jogadores:
    print(Jogador(i))
