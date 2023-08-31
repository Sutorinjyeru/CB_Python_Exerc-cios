# Desenvolva uma classe Bank que gerencia várias contas bancárias.
# Os métodos devem permitir criar novas contas, 
# fazer transferências entre contas e calcular o saldo total do banco.

class Bank:
    def __init__(self, saldo):
        self.saldo = saldo

    #def de criar novas contas
    @classmethod
    def get(cls):
        saldo = int(input("Exemplo de saldo criado\n"))
        return cls(saldo)

    #def de transferência entre contas
    def transfer(obj1, obj2, valor):
        obj1.saldo -= valor
        obj2.saldo += valor
        print(obj1.saldo, obj2.saldo)

    #calcular saldo total
    def total(self, *accounts):
        total = 0
        for _ in range(len(accounts)+1):
            total += self.saldo
        return total

