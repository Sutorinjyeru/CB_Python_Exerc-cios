# Escreva um programa que permita selecionar um aluno aleatório de um arquivo txt.
# Permita que o programa adicione um aluno a lista. Permita que o programa remova
# um aluno da lista.

from random import choice
from time import sleep


def main():
    # Create list with the archive itens
    with open("Archive.txt", "r") as file:
        allStudents = file.read()
        students = list(allStudents.split())

    while True:
        print("Hello User, make your choice! ")
        mode = input(
            "1:Choose a random student, 2:Add student, 3:Remove student")
        if mode == "1":
            random(students)
            sleep(0.5)
        elif mode == "2":
            student = input("eita")
            add(student)
            sleep(0.5)
        elif mode == "3":
            student = input("Ish ")
            remove(students, student)
            sleep(0.5)
        else:
            break


def random(sList=list):
    print(choice(sList))


def add(var=str):
    with open("Archive.txt", "a+") as file:
        file.write("\n"+var)


def remove(sList=list, var=str):
    # Remove All
    with open("Archive.txt", "w") as file:
        file.write("")
    # Create new without the choosen student
    with open("Archive.txt", "a") as file:
        for word in sList:
            file.write(word+"\n")
    sList.remove(var)


if __name__ == "__main__":
    main()
