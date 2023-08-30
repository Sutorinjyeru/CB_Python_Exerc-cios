#Defina uma classe Car com atributos make, model e year.
#Crie um método start_engine que imprime uma mensagem
#indicando que o motor foi iniciado.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("O motor foi iniciado")
    
mustang = Car("sla","sla","nsei")
mustang.start_engine()