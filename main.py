students = {}


def isEmpty(object):
    return bool(object)


def clearScreen():
    print("\x1b[H\x1b[2J")


def printFile(filename):
    file = open(f"txtSrc/{filename}.txt")
    for line in file.readlines():
        print(line)


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
            print()


def showSortedByEmail():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente):")
        for name in sorted(students.values()):
            printStudent(name)
            print()


def searchByName():
    global students

    name = input("Nome do aluno: ")

    if name not in students.keys():
        print("[Erro] Aluno não encontrado.")
    else:
        printStudent(name)


def searchByEmail():
    global students

    email = input("E-mail do aluno: ")

    if email not in students.values():
        print("[Erro] Aluno não encontrado.")
    else:
        printStudent(findKeyByValue(email))


COMMANDS = {
    "help": showHelp,
    "list/r": showSortedByRegister,
    "list/n": showSortedByName,
    "list/e": showSortedByEmail,
    "search/n": searchByName,
    "search/e": searchByEmail,
}

def registerUsers(students):
    try:
        qtdCadastro = int(input("Digite quantos alunos, deseja cadastrar: "))
    except ValueError:
        print("\n[Error]Opção inválida, por favor repita")
        return 
    
    contador = 0
    print("\n" + 10*"_" + f"Cadastro de Usuários" + 10*"_")

    while qtdCadastro != contador:
        name = input("\nDigite o nome completo do aluno: ").title().strip()
        email = input("Digite o e-mail do aluno: ").lower().strip()

        if name != '' and email != '':
            students.update({name : email})
            contador += 1
        else:
            print("[Error]Não cadastramos informações em branco.")
            continue
        
        
def buscarUsuarioEmail(usuarios):
    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        buscar = input('E-mail do aluno: ').lower()
        for usuario in usuarios:
            nome, email = usuario

            if email == buscar:
                print('\nO aluno foi encontrado como:')
                print(f'Nome: {nome}') 
                print(f'E-mail: {email}')
            else:
                print("[Error]E-mail não encontrado")
            break


def deleteStudents():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        buscar = input('E-mail do aluno a ser removido: ').lower()
        for  nome, email in list(students.items()):
            nome = nome
            email = email


            if email == buscar:
                print(f'\nO aluno foi encontrado como:')
                printStudent(nome)
                motivoExclusao = input("\nQual motivo da exclusão?: ")
                atualizar = input("\nDeseja remover o cadastro do aluno?[s/n]: ").lower()
                if atualizar in ['s', 'sim', 'y', 'yes']:
                    students.pop(nome)
                    print(f"\nO cadastro do aluno foi excluído")
                elif atualizar in ['n', 'nao', 'no', 'não']:
                    print("\nVoltando ao menu")
                else:
                    print("\n[Error]Não entendi, pode repetir?")
                    continue
                with open(r'\txtSrc\deleted.txt','a') as deleteds:
                    deleteds.write(f'Nome: {nome}, Email: {email}, Motivo {motivoExclusao}\n')


            else:
                print(f'[Error]E-mail não encontrado')
            break


def showDeletedRegisters():
    printFile(r'\txtSrc\deleted')
    clearDeleted = input("Deseja limpar a lista?")
    if clearDeleted in ['s', 'sim', 'y', 'yes']:
        with open(r'\txtSrc\deleted.txt','w'):
            pass
    

def updateStudents():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        buscar = input("E-mail do aluno a ser atualizado: ").lower().strip()
        for  nome, email in list(students.items()):
            nome = nome
            email = email
            if email == buscar:
                print(f'\nO aluno foi encontrado como:')
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
