#Crie uma classe Student com atributos name, age e grades (uma lista).
#Adicione métodos para adicionar notas, calcular a média das notas e exibir
#as informações do aluno.

class Student():
    def __init__(self, name, age, grades=list):
        self.name = name
        self.age = age
        self.grades = grades
    
    def add_notes(self):
        num = int(input("Quantas notas?: "))
        for _ in range(num):
            notas = int(input("Digite qual foi a nota: "))
            self.grades.append(notas)
        return self.grades
    
    def average(self, result):
        result = 0
        for i in self.grades:
            result += i
        return result / len(self.grades)
            
    def infos(self, average):
        print(self.name, self.age, *self.grades)

notas = []
aluno = Student("Leon", 15, notas)
aluno.average(aluno.add_notes())