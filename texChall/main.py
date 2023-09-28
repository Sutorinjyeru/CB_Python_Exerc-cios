# Escreva um programa que permita selecionar
# um aluno aleatório de um arquivo txt.
# Permita que o programa adicione um aluno a lista.
# Permita que o programa remova
# um aluno da lista.

#Erros
#GUI
from random import choice
import PySimpleGUI as sg

sg.theme('')

def main():
    # Create list with the archive itens
    with open("Archive.txt") as file:
        allStudents = file.read()
        students = allStudents.split()

    while True:
        print("Hello User, make your choice!")
        mode = input(
            "1:Choose a random student, 2:Add student, 3:Remove student, 4:Close\n")
        if mode == "1":
            random(students)
        elif mode == "2":
            student = input("Type the name you want to add.\n")
            add(students, student)
        elif mode == "3":
            student = input("Type the name you want to remove.\n")
            remove(students, student)
        elif mode == "4":
            file.close()
            break


def random(sList=list):
    print(choice(sList))


def add(sList=list,var=str):
    # Remove All
    with open("Archive.txt", "w") as file:
        file.write("")
    #Create new
    with open("Archive.txt", "a") as file:
        sList.append(var)
        for name in sList:
            file.write(name+"\n")    


def remove(sList=list, var=str):
    with open("Archive.txt") as file1:
        items = file1.read()
        newList = items.split()
    #Remove All
    with open("Archive.txt", "w") as file:
        file.write("")
    #Create new
    try:
        with open("Archive.txt", "a") as file:
            sList.remove(var)
            for name in sList:
                file.write(name+"\n")
    except ValueError:
        print("Name not in list, try again. ")
        with open("Archive.txt", "w") as file1:
            for i in newList:
                file1.write(i+"\n")


if __name__ == "__main__":
    main()
