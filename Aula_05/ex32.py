# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando sua mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# Pedindo input do usuário
grade1 = float(input("Primeira nota\n"))
grade2 = float(input("Segunda nota\n"))

# Cálculo da média
average = (grade1 + grade2) * 2

# Verificando a situação do aluno
if average < 5.0:
    print("REPROVADO")
elif average >= 5.0 and average <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")