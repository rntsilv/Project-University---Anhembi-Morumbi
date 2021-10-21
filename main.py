students = {}


def isEmpty(object):
    return bool(object)


def clearScreen():
    print("\x1b[H\x1b[2J")


def printFile(filename):
    file = open(f"txtSrc/{filename}.txt")
    for line in file.readlines():
        print(line, end="")


def storeRemoved(name, email, reason):
    with open("txtSrc/deleted.txt", "a") as file:
        file.write(f"Nome: {name}\nE-mail: {email}\nMotivo: {reason}\n")


def clearRemoved():
    with open("txtSrc/deleted.txt", mode="w", encoding="utf-8"):
        pass


def printRemoved():
    printFile("deleted")


def showHelp():
    printFile("help")


def findKeyByValue(value):
    global students

    if value not in students.values():
        return None
    else:
        return students.keys()[students.values().index(value)]


def printStudent(name):
    global students

    print("Nome :", name, "\n")
    print("E-mail: ", students[name])


def showSortedByRegister():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente):")
        for name in students.values():
            printStudent(name)


def showSortedByName():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente):")
        for name in sorted(students.keys()):
            printStudent(name)


def showSortedByEmail():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente):")
        for name in sorted(students.values()):
            printStudent(name)


def searchByName():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
        return

    name = input("Nome do aluno: ")
    if name not in students.keys():
        print("[Erro] Aluno não encontrado.")
    else:
        printStudent(name)


def searchByEmail():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
        return

    email = input("E-mail do aluno: ").strip().lower()
    if email not in students.values():
        print("[Erro] Aluno não encontrado.")
    else:
        printStudent(findKeyByValue(email))


def registerStudent():
    global students

    registerAmount = 0
    try:
        registerAmount = int(input("Digite quantos alunos, deseja cadastrar: "))
    except ValueError:
        print("\n[Error]Opção inválida, por favor repita")
        return 
    
    for _i in range(registerAmount):
        name = input("Digite o nome completo do aluno: ").strip().title()
        email = input("Digite o e-mail do aluno: ").strip().lower()

        if isEmpty(name) or isEmpty(email):
            print("[Erro] Não cadastramos informações em branco.")
        else:
            students.update({name: email})


def removeByName():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
        return

    name = input("Nome do aluno a ser removido: ").strip().title()
    if name not in students.keys():
        print("[Erro] Aluno não encontrado.")
    else:
        reason = input("Motivo da exclusão: ")
        storeRemoved(name, students[name], reason)
        del students[name]


def removeByEmail():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
        return

    email = input("E-mail do aluno a ser removido: ").strip().lower()
    name = findKeyByValue(email)
    if name not in students.keys():
        print("[Erro] Aluno não encontrado.")
    else:
        reason = input("Motivo da exclusão: ")
        storeRemoved(name, students[name], reason)
        del students[name]


def updateName():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
        return

    name = input("Nome do aluno a ser atualizado: ").strip().title()
    if name not in students.keys():
        print("[Erro] Aluno não encontrado.")
    else:
        newName = input("Novo nome: ").strip().title()
        students[newName] = students[name]
        del students[name]


def updateEmail():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
        return

    email = input("E-mail do aluno a ser atualizado: ").strip().lower()
    if email not in students.values():
        print("[Erro] Aluno não encontrado.")
    else:
        newEmail = input("Novo e-mail: ").strip().lower()
        students[findKeyByValue(email)] = newEmail


def stopExecution():
    exit()
        
        
COMMANDS = {
    "help": showHelp,
    "register": registerStudent,
    "list/r": showSortedByRegister,
    "list/n": showSortedByName,
    "list/e": showSortedByEmail,
    "list/b": printRemoved,
    "clearbin": clearRemoved,
    "search/n": searchByName,
    "search/e": searchByEmail,
    "remove/n": removeByName,
    "remove/e": removeByEmail,
    "update/n": updateName,
    "update/e": updateEmail,
    "end": stopExecution,
}

COMMAND_LIST = COMMANDS.keys()


def queryCommand():
    chosenCommand = input("> ").strip().lower()
    if chosenCommand not in COMMAND_LIST:
        print("[Erro] Comando não encontrado.")
    else:
        print()
        COMMANDS[chosenCommand]()
        print()


def main():
    while True:
        queryCommand()


if __name__ == "__main__":
    main()
