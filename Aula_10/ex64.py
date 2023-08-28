# Crie uma função chamada "read_file" que recebe o nome de
# um arquivo e tenta abrí-lo para leitura.
# Se o arquivo não existir, capture a excessão
# FileNotFoundError e imprima uma mensagem amigável para o usuário.

def main():
    file = input("Archive ")
    read_file(file)

def read_file(arq_N):
    try:
        open(arq_N,"r")
    except FileNotFoundError:
        print("Num deu")

main()