import time


def clearScreen():
    print("\x1b[2J\x1b[H")


def loginAdm():
    clearScreen()
    tentativasLogin = 0
    print('\nPara continuar, digite seu login de Gestor')
    while True:
        tentativasLogin += 1
        if tentativasLogin > 3:
            print("\nUsuário Bloqueado, tente novamente mais tarde")
            exit()
        else:
            login = open(r'txt\login.txt')
            senha = open(r'txt\senha.txt')

            usuarioLogin = input('\nDigite o seu nome de usuário: ').lower()
            usuarioSenha = input('Digite a sua senha: ')

            usuario = login.readlines()
            password = senha.readlines()
            if usuarioLogin in usuario and usuarioSenha in password:
                print(f'Bem-vindo, {usuarioLogin}!')
                time.sleep(1.5)
                return False
            else:
                print('\nVocê deve ter digitado seu nome de usuario errado, por favor verifique.Numero de tentativas restante {}'.format(3-tentativasLogin))
            login.close()
            senha.close()


def cadastrarUsuarios(usuarios):
    while True:
        try:
            qtdCadastro = int(input("Digite quantos alunos, deseja cadastrar: "))
            contador = 0
            print("\n" + 10*"_" + f"Cadastro de Usuários" + 10*"_")

            while qtdCadastro != contador:
                nome = input("\nDigite o nome completo do aluno: ").lower()
                email = input("Digite o e-mail do aluno: ").lower()

                if nome != '' and email != '':
                    usuarios.append((nome.title(), email))
                    contador += 1
                else:
                    print("[Error]Preencha corretamente seus dados")    
                    continue   
            break

        except ValueError:
            print("\n[Error]Opção inválida, por favor repita")
            break


def exibirOrdemAlfabetica(usuarios):

    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        usuariosSorteados = sorted(usuarios)

        print("\n" + 13*"_" + f"Ordem Alfabética" + 13*"_")
        for usuario in usuariosSorteados:
            print(f'\nNome: {usuario[0]}\nE-mail: {usuario[1]}')


def usuariosCadastrados(usuarios):
    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        print("\n" + 13*"_" + f"Usuários" + 13*"_")
        for usuario in usuarios:
            nome, email = usuario
            print(f'\nNome: {nome}\nE-mail: {email}')


def buscarUsuarioEmail(usuarios):
   
    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        buscar = input('E-mail do aluno: ').lower()
        for usuario in usuarios:
            nome, email = usuario

            if email == buscar:
                print(f'\nO aluno foi encontrado como > Nome: {nome} com o Email: {email}')
                break
        else:
            print("[Error]E-mail não encontrado")


def removerUsuarios(usuarios, usuariosExcluidos):
    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        buscar = input('E-mail do aluno a ser removido: ').lower()
        for usuario in usuarios:
            nome, email = usuario

            if email == buscar:
                print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')
                motivoExclusao = input("Qual motivo da exclusão?: ")
                atualizar = input("\nDeseja remover o cadastro do aluno?[s/n]: ").lower()
                excluidos = {'nome': nome,'email': email,'motivo': motivoExclusao}
                if atualizar in ['s', 'sim', 'y', 'yes']:
                    excluir = usuarios.index(usuario)
                    usuariosExcluidos.append(excluidos)
                    usuarios.pop(excluir)
                    print(f"\nO cadastro do aluno foi excluído")
                    break
                elif atualizar in ['n', 'nao', 'no', 'não']:
                    print("\nVoltando ao menu")
                    break
                else:
                    print("\n[Error]Não entendi, pode repetir?")
                    continue
        else:
            print(f'[Error]E-mail não encontrado')  

def exibirUsuariosExcluidos(usuariosExcluidos):
    if usuariosExcluidos == []:
        print("[Error] Lista vazia!")
    else:
        print("\n" + 13*"_" + f"Usuários Excluidos" + 13*"_")
        for usuario in usuariosExcluidos:           
            print("Nome: {}, Email: {}, Motivo: {}".format(usuario['nome'], usuario['email'], usuario['motivo']))


def atualizarUsuarios(usuarios):
    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        buscar = input("E-mail do aluno a ser atualizado: ")
        for i,usuario in enumerate(usuarios):
            nome, email = usuario

            if email == buscar:
                print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')

                novoNome = input("\nDigite o novo nome a ser colocado no seu cadastro: ").lower()

                excluir = usuarios.index(usuario)
                usuarios.pop(excluir)

                novoUsuario = novoNome.title(), email

                usuarios.insert(i, novoUsuario)
                print(f"\nO nome do Aluno foi atualizado")
                break
        else:
            print("[Error]E-mail não encontrado")

def atualizarEmail(usuarios):
    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        buscar = input("Digite o nome completo do aluno que deseja atualizar o e-mail: ").title()
        for i,usuario in enumerate(usuarios):
            nome, email = usuario
            if nome == buscar:
                    print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')

                    novoEmail = input("\nDigite o novo e-mail a ser colocado no seu cadastro: ").lower()

                    excluir = usuarios.index(usuario)
                    usuarios.pop(excluir)

                    novoUsuario = nome, novoEmail

                    usuarios.insert(i, novoUsuario)
                    print(f"\nO e-mail do Aluno foi atualizado")
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

    menuOpcoes['1']="[1] Para cadastrar um novo aluno" 
    menuOpcoes['2']="[2] Para exibir a lista de alunos(Por ordem de cadastro)"
    menuOpcoes['3']="[3] Para exibir a lista de aluno(Por ordem Alfabética)"
    menuOpcoes['4']="[4] Para buscar um aluno por e-mail de cadastro"
    menuOpcoes['5']="[5] Para remover o cadastro de um aluno"
    menuOpcoes['6']="[6] Para atualizar o nome de um aluno"
    menuOpcoes['7']="[7] Para atualizar o e-mail de um aluno"
    menuOpcoes['8']="[8] Para exibir os alunos excluidos"
    menuOpcoes['9']="[9] Para encerrar o programa"

    while True:
        clearScreen()
        opcoes = menuOpcoes.values()
        print()
        print("\n" + 28 * "_" + "MENU" + 28 * "_")
        print()

        for escolha in opcoes:
            print(escolha)

        print(60 * "_")

        selection = input("Escolha uma opção: ")
        
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
    loginAdm()
    while True:
        menu()


if __name__ == "__main__":
    main()
