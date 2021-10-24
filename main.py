import config

students = {}

def storeRemoved(name, email, reason):
    with open("txtSrc/deleted.txt", mode="a", encoding="utf-8") as file:
        file.write(f"Nome: {name}\nE-mail: {email}\nMotivo: {reason}\n")


def clearRemoved():
    with open("txtSrc/deleted.txt", mode="w", encoding="utf-8") as file:
        file.write("")

def printRemoved():
    config.printFile("deleted")


def showHelp():
    config.printFile("help")


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

    if config.isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada por cadastro):")
        for name in students.values():
            printStudent(findKeyByValue(name))


def showSortedByName():
    global students

    if config.isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente por Nome):")
        for name in sorted(students.keys()):
            printStudent(name)


def showSortedByEmail():
    global students

    if config.isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente por E-mail):")
        for email in sorted(students.values()):
            printStudent(findKeyByValue(email))


def searchByName():
    global students

    if config.isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
        return

    name = input("Nome do aluno: ")
    if name not in students.keys():
        print("[Erro] Aluno não encontrado.")
    else:
        printStudent(name)


def searchByEmail():
    global students

    if config.isEmpty(students):
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

        if config.isEmpty(name) or config.isEmpty(email):
            print("[Erro] Não cadastramos informações em branco.")
        else:
            students.update({name: email})


def removeByName():
    global students

    if config.isEmpty(students):
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

    if config.isEmpty(students):
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

    if config.isEmpty(students):
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

    if config.isEmpty(students):
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
    config.inputFile("login", newUsername)


def updatePassword():
    print("Obs: A senha precisa ter entre 4 e 8 digitos\n")
    newPassword = input("Digite a nova senha do administrador: ")
    if len(newPassword) >= 4 and len(newPassword) <= 8:
        config.inputFile("senha", newPassword)
    else:
        print("[Error] Não foi possivel cadastrar essa senha")


def restoreLogin():
    config.inputFile("login", config.defaultLogin)
    config.inputFile("senha", config.defaultPassword)
    print("Login de administrador restaurado")


def encryptPassword():
    encryptpassword = config.encrypt(config.openFile("senha"))
    config.inputFile("senha", encryptpassword)
    config.animated("Criptografando")
    print(f"\nSua senha encriptografada é: {encryptpassword}")


def descryptPassword():
    descryptpassword = config.descrypt(config.openFile("senha"))
    config.animated("Descriptografando")
    config.inputFile("senha", descryptpassword)
    print(f"\nSua senha descriptografada é: {descryptpassword}")


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
    "update/c": encryptPassword,
    "update/d": descryptPassword,
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
    config.loginAdm()
    while True:
        queryCommand()


if __name__ == "__main__":
    main()
