#Defina uma classe BankAccount com atributos privados balance e account_number.
#Crie métodos deposit e withdraw para manipular o saldo.

class BankAccount():
    def __init__(self, balance, account_number) -> None:
        self.__balance = balance
        self.__account_number = account_number
    
    def deposit(self, quantity):
        self.__balance += quantity
        print(f"O Saldo atual da conta{self.__account_number} é:{self.__balance}")
    
    def withdraw(self, quantity):
        self.__balance -= quantity
        print(f"O Saldo atual da conta{self.__account_number} é:{self.__balance}")

account1 = BankAccount(3000, 123)
account1.withdraw(300)