usuarios = []

def loginAdm():
    cont = 0
    print('\nPara continuar, digite seu login de Gestor')
    while True:
        cont += 1
        if cont > 3:
            print("\nUsuario Bloqueado, tente novamente mais tarde")
            exit()
        else:
            login = open('txt\login.txt')
            senha = open('txt\senha.txt')

            usuarioLogin = input('\nDigite o seu nome de usuario: ').lower()
            usuarioSenha = input('Digite a sua senha: ')

            usuario = login.readlines()
            password = senha.readlines()
            if usuarioLogin in usuario and usuarioSenha in password:
                print(f'Bem vindo, {usuarioLogin}!')
                return False
            else:
                print('\nVocê deve ter digitado seu nome de usuario errado, por favor verifique.')
            login.close()
            senha.close()


def cadastrarUsuarios():
    global usuarios

    while True:
        try:
            qtdCadastro = int(input("Quantos alunos deseja cadastrar?: "))
            contador = 0
            print("\n" + 10*"_" + f"Cadastro de Usuários" + 10*"_")

            while qtdCadastro != contador:
                nome = input("\nDigite o nome do aluno: ").lower()
                email = input("Digite o e-mail do aluno: ").lower()
                usuarios.append((nome, email))
                contador += 1
                
            break

        except ValueError:
            print("[Error]Não entendi, repita")
            break


def exibirOrdemAlfabetica():
    global usuarios

    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        usuariosSorteados = sorted(usuarios)

        print("\n" + 13*"_" + f"Ordem Alfabetica" + 13*"_")
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


def buscarUsuarioEmail():
    global usuarios
    buscar = input('E-mail do aluno: ')

    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        for usuario in usuarios:
            nome, email = usuario

            if email == buscar:
                print(f'\nO aluno foi encontrado como > Nome: {nome}, E-mail: {email}')
                break
            else:
                print(f'[Error]E-mail não encontrado')
                break



def removerUsuarios():
    global usuarios
    buscar = input('E-mail do aluno: ')

    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        for usuario in usuarios:
            nome, email = usuario

            if email == buscar:
                print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')
        
                atualizar = input("\nDeseja remover o cadastro do aluno?[s/n]: ").lower()

                if atualizar in ['s', 'sim']:
                    excluir = usuarios.index(usuario)
                    usuarios.pop(excluir)
                    print(f"\nO cadastro do aluno foi excluido")
                    break
                elif atualizar in ['n', 'nao', 'no', 'não']:
                    print("\nVoltando ao menu")
                    break
                else:
                    print("\n[Error]Não entendi, pode repetir?")
                    continue
            else:
                print(f'[Error]E-mail não encontrado')
                break


def atualizarUsuarios():
    global usuarios

    buscar = input("E-mail do usuário a ser removido: ")

    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        for usuario in usuarios:
            nome, email = usuario

            if email == buscar:
                print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')

                novoNome = input("\nDigite o novo nome a ser colocado no seu cadastro: ")
                excluir = usuarios.index(usuario)
                usuarios.pop(excluir)
                usuarios.append((novoNome, email))
                print(f"\nO nome do Aluno foi atualizado")
                break
            else:
                print(f'[Error]E-mail não encontrado')
                break


def back():
    while True:
        back = str(input('\nPRESSIONE "ENTER" PARA VOLTAR AO MENU'))
        if not back:
            return False


def menu():
    print()
    print("\t\tBEM VINDO AO MENU")
    print("\n" + 23 * "_" + "MENU" + 23 * "_")
    print("[1] Para cadastrar um novo aluno")
    print("[2] Para exibir a lista de alunos(Por ordem de cadastro)")
    print("[3] Para exibir a lista de aluno(Por ordem Alfabética)")
    print("[4] Para buscar um aluno por e-mail de cadastro")
    print("[5] Para remover o cadastro de um aluno")
    print("[6] Para atualizar o nome de um aluno")
    print("[7] Para encerrar o programa")
    print(50 * "_")

    opcao = int(input('\nQual a sua ação: '))
    
    if opcao == 1:
        cadastrarUsuarios()
        back()
    elif opcao == 2:
        usuariosCadastrados(usuarios)
        back()
    elif opcao == 3:
        exibirOrdemAlfabetica()
        back()
    elif opcao == 4:
        buscarUsuarioEmail()
        back()
    elif opcao == 5:
        removerUsuarios()
        back()
    elif opcao == 6:
        atualizarUsuarios()
        back()
    elif opcao == 7:
        exit()
    else:
        print('Ação inválida')


def main():
    loginAdm()
    while True:
        menu()


if __name__ == "__main__":
    main()
