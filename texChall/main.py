# Escreva um programa que permita selecionar
# um aluno aleatório de um arquivo txt.
# Permita que o programa adicione um aluno a lista.
# Permita que o programa remova
# um aluno da lista.

import PySimpleGUI as sg
# Erros
# GUI
from Class import Manager as Mg
from Layout import Menu as M


def main():
    # Create list with the archive itens
    with open("Archive.txt") as file:
        allStudents = file.read()
        students = allStudents.split()
    while True:
        event, values = M.window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == 'Choose a random student':
            M.window.close()
            event, values = M.window2.read()
            Mg.random_student(students)
        if event == 'Add student':
            M.window.close()
            event, values = M.window3.read()
            Mg.add_student(students, values[0])
        if event == 'Remove Student':
            M.window.close()
            event, values = M.window4.read()
            Mg.remove_student(students, values[0])

    M.window.close()


if __name__ == "__main__":
    main()
