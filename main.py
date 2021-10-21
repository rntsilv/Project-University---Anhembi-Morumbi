students = {}


def isEmpty(object):
    return bool(object)


def clearScreen():
    print("\x1b[H\x1b[2J")


def printFile(filename):
    file = open(f"txtSrc/{filename}.txt")
    for line in file.readlines():
        print(line)


def storeRemoved(name, email, reason):
    with open("txtSrc/deleted.txt", "a") as file:
        file.write(f"Nome: {name}\nE-mail: {email}\nMotivo: {reason}\n")


def clearRemoved():
    with open("txtSrc/deleted.txt", "w"):
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

    name = input("Nome do aluno: ")

    if name not in students.keys():
        print("[Erro] Aluno não encontrado.")
    else:
        printStudent(name)


def searchByEmail():
    global students

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

    name = input("Nome do aluno a ser removido: ").strip().title()

    if name not in students.keys():
        print("[Erro] Aluno não encontrado.")
    else:
        reason = input("Motivo da exclusão: ")
        storeRemoved(name, students[name], reason)
        del students[name]


def removeByEmail():
    global students

    email = input("E-mail do aluno a ser removido: ").strip().lower()
    name = findKeyByValue(email)

    if name not in students.keys():
        print("[Erro] Aluno não encontrado.")
    else:
        reason = input("Motivo da exclusão: ")
        storeRemoved(name, students[name], reason)
        del students[name]


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
    "end": stopExecution,
}


def updateStudents():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        buscar = input("E-mail do aluno a ser atualizado: ").strip().lower()
        for nome, email in students.items():
            if email == buscar:
                print("\nO aluno foi encontrado como:")
                printStudent(nome)
                while True:
                    novoNome = input("\nDigite o novo nome a ser colocado no seu cadastro: ").title().strip()
                    if novoNome != "":
                        students[novoNome] = students.pop(nome)
                        print(f"\nO nome do aluno foi atualizado, com sucesso.")
                        break
                    else:
                        print("[Error]Não salvamos espaço em branco amigo")
                        continue
                break
        else:
            print("[Error]E-mail não encontrado")


def updateEmail():
    global students

    if isEmpty(students):
        print("[Error]Nenhum aluno cadastrado")
    else:
        buscar = input("Digite o e-mail para ser atualizado: ").lower().strip()
        for nome, email in list(students.items()):
            nome = nome
            email = email
            if email == buscar:
                print(f'\nO aluno foi encontrado como:')
                printStudent(nome)
                printStudent(email)
                while True:
                    novoEmail = input("\nDigite o novo e-mail para ser atualizado: ").title().strip()
                    if novoEmail != "":
                        students[novoEmail] = students.pop(email)
                        print(f"\nO e-mail do aluno foi atualizado, com sucesso.")
                        break
                    else:
                        print("[Error]Não salvamos espaço em branco amigo")
                        continue
                break
        else:
            print("[Error]E-mail não encontrado")

    
def back():
    while True:
        back = str(input('\nPRESSIONE "ENTER" PARA VOLTAR AO MENU'))
        if not back:
            return False


def menu():
    usuarios = []
    usuariosExcluidos = []
    menuOpcoes = {}

    while True:
        clearScreen()
        opcoes = menuOpcoes.values()
        print("\n\n" + 28 * "_" + "MENU" + 28 * "_" + "\n")

        for escolha in opcoes:
            print(escolha)

        print(60 * "_")

        selection = input("\nEscolha uma opção: ")
        
        if selection =='1':
            registerUsers(usuarios)
        elif selection == '2':
            usuariosCadastrados(usuarios)
        elif selection == '3':
            exibirOrdemAlfabetica(usuarios)
        elif selection == '4': 
            buscarUsuarioEmail(usuarios)
        elif selection == '5': 
            removerUsuarios(usuarios,usuariosExcluidos )
        elif selection == '6': 
            atualizarUsuarios(usuarios)
        elif selection == '7': 
            updateEmail(usuarios)
        elif selection == '8':
            exibirUsuariosExcluidos(usuariosExcluidos)    
        elif selection == '9': 
            exit()
        else: 
            print("[Error]Opção inválida")

        back()


def main():
    while True:
        menu()


if __name__ == "__main__":
    main()
