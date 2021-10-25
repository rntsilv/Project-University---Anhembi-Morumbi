import config, utils, files, console

students = {}


def storeRemoved(name, email, reason):
    with open("txtSrc/deleted.txt", mode="a", encoding="utf-8") as file:
        file.write(f"Nome: {name}\nE-mail: {email}\nMotivo: {reason}\n")


def clearRemoved():
    with open("txtSrc/deleted.txt", mode="w", encoding="utf-8") as file:
        file.write("")


def printRemoved():
    files.printFile("deleted")


def showHelp():
    files.printFile("help")


def findKeyByValue(value):
    global students

    if value not in students.values():
        return None
    else:
        return list(students.keys())[list(students.values()).index(value)]


def printStudent(name):
    global students

    print(f"Nome: {name}\nE-mail: {students[name]}")


def showSortedByRegister():
    global students

    if utils.isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada por cadastro):")
        for name in students.values():
            printStudent(findKeyByValue(name))


def showSortedByName():
    global students

    if utils.isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente por Nome):")
        for name in sorted(students.keys()):
            printStudent(name)


def showSortedByEmail():
    global students

    if utils.isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente por E-mail):")
        for email in sorted(students.values()):
            printStudent(findKeyByValue(email))


def searchByName():
    global students

    if utils.isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
        return

    name = input("Nome do aluno: ")
    if name not in students.keys():
        print("[Erro] Aluno não encontrado.")
    else:
        printStudent(name)


def searchByEmail():
    global students

    if utils.isEmpty(students):
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
        print("\n[Error] Opção inválida, por favor tente novamente mais tarde.")
        return 
    
    for _i in range(registerAmount):
        name = input("Digite o nome completo do aluno: ").strip().title()
        email = input("Digite o e-mail do aluno: ").strip().lower()

        if utils.isEmpty(name) or utils.isEmpty(email):
            print("[Erro] Não cadastramos informações em branco.")
        else:
            students.update({name: email})


def removeByName():
    global students

    if utils.isEmpty(students):
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

    if utils.isEmpty(students):
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

    if utils.isEmpty(students):
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

    if utils.isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
        return

    email = input("E-mail do aluno a ser atualizado: ").strip().lower()
    if email not in students.values():
        print("[Erro] Aluno não encontrado.")
    else:
        newEmail = input("Novo e-mail: ").strip().lower()
        students[findKeyByValue(email)] = newEmail


def updateUsername():
    newUsername = input("Digite o novo login do administrador: ")
    files.inputFile("login", newUsername)


def updatePassword():
    print("Obs: A senha precisa ter entre 4 á 8 digitos\n")
    newPassword = input("Digite a nova senha do administrador: ")
    if len(newPassword) >= 4 and len(newPassword) <= 8:
        files.inputFile("senha", config.encrypt(newPassword))
        console.animated("Criptografando senha")
    else:
        print("[Erro] Não foi possivel cadastrar essa senha")


def restoreLogin():
    files.inputFile("login", config.defaultLogin)
    files.inputFile("senha", config.encrypt(config.defaultPassword))
    console.animated("Restaurando")
    print("Login de administrador restaurado")


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
    "restore/a": restoreLogin,
    "update/n": updateName,
    "update/e": updateEmail,
    "update/l": updateUsername,
    "update/p": updatePassword,
    "end": stopExecution,
}

COMMAND_LIST = COMMANDS.keys()


def queryCommand():
    print("Digite \"help\" para ver o menu de opções")
    chosenCommand = input("\n> ").strip().lower()
    if chosenCommand not in COMMAND_LIST:
        print("[Erro] Comando não encontrado.")
    else:
        print()
        COMMANDS[chosenCommand]()
        print()


def main():
    console.clearScreen()
    config.loginAdm()
    console.clearScreen()
    while True:
        queryCommand()


if __name__ == "__main__":
    main()
    
    
