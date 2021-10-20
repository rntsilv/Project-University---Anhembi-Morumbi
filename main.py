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


def showSortedRegister():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente):")
        for name in students.values():
            print(f"Nome: ", name, "\n")
            print(f"E-mail: ", students[name], "\n\n")


def showSortedName():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente):")
        for name in sorted(students.keys()):
            print(f"Nome: ", name, "\n")
            print(f"E-mail: ", students[name], "\n\n")


def showSortedEmail():
    global students

    if isEmpty(students):
        print("[Erro] Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos (ordenada alfabeticamente):")
        for name in sorted(students.values()):
            print(f"Nome: ", name, "\n")
            print(f"E-mail: ", students[name], "\n\n")


COMMANDS = {
    "help": showHelp,
    "list/r": showSortedRegister,
    "list/n": showSortedName,
    "list/e": showSortedEmail,
}


def cadastrarUsuarios(usuarios):
    while True:
        try:
            qtdCadastro = int(input("Digite quantos alunos, deseja cadastrar: "))
            contador = 0
            print("\n" + 10*"_" + f"Cadastro de Usuários" + 10*"_")

            while qtdCadastro != contador:
                nome = input("\nDigite o nome completo do aluno: ").title()
                email = input("Digite o e-mail do aluno: ").lower()

                if nome != '' and email != '':
                    usuarios.append((nome.strip(), email.strip()))
                    contador += 1
                else:
                    print("[Error]Não salvamos espaço em branco amigo")    
                    continue   
            break

        except ValueError:
            print("\n[Error]Opção inválida, por favor repita")
            break


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


def removerUsuarios(usuarios, usuariosExcluidos):
    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        buscar = input('E-mail do aluno a ser removido: ').lower()
        for usuario in usuarios:
            nome, email = usuario

            if email == buscar:
                print(f'\nO aluno foi encontrado como:')
                print(f'Nome: {nome}') 
                print(f'E-mail: {email}')
                motivoExclusao = input("\nQual motivo da exclusão?: ")
                atualizar = input("\nDeseja remover o cadastro do aluno?[s/n]: ").lower()
                excluidos = {'nome': nome,'email': email,'motivo': motivoExclusao}
                if atualizar in ['s', 'sim', 'y', 'yes']:
                    excluir = usuarios.index(usuario)
                    usuariosExcluidos.append(excluidos)
                    usuarios.pop(excluir)
                    print(f"\nO cadastro do aluno foi excluído")
                elif atualizar in ['n', 'nao', 'no', 'não']:
                    print("\nVoltando ao menu")
                else:
                    print("\n[Error]Não entendi, pode repetir?")
                    continue
            else:
                print(f'[Error]E-mail não encontrado')
            break


def exibirUsuariosExcluidos(usuariosExcluidos):
    if usuariosExcluidos == []:
        print("[Error] Lista vazia!")
    else:
        print("\n" + 13*"_" + f"Usuários Excluídos" + 13*"_")
        for usuario in usuariosExcluidos:           
            print("\nNome: {}\nE-mail: {}\nMotivo: {}".format(usuario['nome'], usuario['email'], usuario['motivo']))


def atualizarUsuarios(usuarios):
    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        buscar = input("E-mail do aluno a ser atualizado: ").lower().strip()

        for i,usuario in enumerate(usuarios):
            nome, email = usuario

            if email == buscar:
                print(f'\nO aluno foi encontrado como:')
                print(f'Nome: {nome}') 
                print(f'E-mail: {email}')


                while True:
                    novoNome = input("\nDigite o novo nome a ser colocado no seu cadastro: ").title()

                    if novoNome != "":
                        excluir = usuarios.index(usuario)
                        usuarios.pop(excluir)

                        novoUsuario = novoNome.strip(), email

                        usuarios.insert(i, novoUsuario)
                        print(f"\nO nome do aluno foi atualizado, com sucesso.")
                        break
                    else:
                        print("[Error]Não salvamos espaço em branco amigo")
                        continue
                break
        else:
            print("[Error]E-mail não encontrado")


def atualizarEmail(usuarios):
    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        buscar = input("Nome do aluno a ser atualizado: ").title().strip()

        for i,usuario in enumerate(usuarios):
            nome, email = usuario

            if nome == buscar:
                print(f'\nO aluno foi encontrado como:')
                print(f'Nome: {nome}')
                print(f'E-mail: {email}')

                while True:
                    novoEmail = input("\nDigite o novo e-mail a ser colocado no seu cadastro: ").lower()

                    if novoEmail != "":
                        excluir = usuarios.index(usuario)
                        usuarios.pop(excluir)

                        novoUsuario = nome, novoEmail.strip()

                        usuarios.insert(i, novoUsuario)
                        print(f"\nO e-mail do aluno foi atualizado, com sucesso.")
                        break
                    else:
                        print("[Error]Não salvamos espaço em branco amigo")
                        continue
                break
        else:
            print("[Error]Nome não encontrado")

    
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
            cadastrarUsuarios(usuarios)
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
            atualizarEmail(usuarios)
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
