# Crie uma classe Employee com atributos name, position e salary.
# Adicione um método apply_raise que aumenta o salário do 
# funcionário em uma determinada porcentagem.

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def apply_raise(self, perc):
        return self.salary + (self.salary * perc)