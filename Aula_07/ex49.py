# Faça um algoritmo que leia um numero inteiro e mostre os
# N primeiros algorismos de uma sequencia fibonacci
seq = int(input("Sequência"))


def fibo(x):
    count = 0
    t1= 1
    t2 = 1
    while count < seq:
        s = t1 + t2
        t1 = t2
        t2 = s
        print(s)
        count += 1
fibo(seq)