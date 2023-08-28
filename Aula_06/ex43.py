# Monte um código para dizer se o número informado é primo

num = int(input("Dê um número: "))
isP = 0
for i in range (2, num):
    if num % 1 == 0 and num % num == 0:
        if not num % i != 0:
            isP = 1

if isP == 1:
    print("Não é primo")
else:
    print("É primo")