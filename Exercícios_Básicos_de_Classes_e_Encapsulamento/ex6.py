# Desenvolva uma classe Book com atributos title, author e year.
# Implemente um método get_age que retorna quantos anos o 
# livro tem desde o ano atual.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_age(self):
        return 2023 - self.year
