
def cadastrarUsuarios(usuarios):
    qtdCadastro = int(input("Quantos alunos deseja cadastrar? "))
    contador = 0
    while qtdCadastro != contador:
        print("\n" + 13*"_" + f"usuario({contador+1})" + 13*"_")
        nome = input("\nDigite o nome do aluno: ").lower()
        email = input("Digite o e-mail do aluno: ").lower()
        usuarios.append((nome, email))

        contador += 1


def exibirOrdemAlfabetica(usuarios):

    cont = 0
    if usuarios != []:
        for usuario in usuarios:
            nome, email = usuario
            print("\n" + 13*"_" + f"usuario({cont})" + 13*"_")
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            cont += 1
    else:
        print("[Error]Não existe nenhum aluno cadastrado")

def usuariosCadastrados(usuarios):
    cont = 0
    if usuarios != []:
        for usuario in usuarios:
            nome, email = usuario
            print("\n" + 13*"_" + f"usuario({cont})" + 13*"_")
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            cont += 1
    else:
        print("[Error]Não existe nenhum aluno cadastrado")


def buscarUsuarioEmail(usuarios):
    
    buscar = input('E-mail do aluno: ')
    for usuario in usuarios:
        nome, email = usuario
        if email == buscar:
            print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')
            break
    else:
        print(f'[Error]Aluno não encontrado')

def removerUsuarios(usuarios):
    buscar = input('E-mail do aluno: ')

    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        for usuario in usuarios:
            nome, email = usuario
            if email == buscar:
                print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')
                break     

    atualizar = input("\nDeseja remover o cadastro do aluno?[s/n]: ").lower()

    if atualizar in ['s', 'sim']:
        excluir = usuarios.index(usuario)
        usuarios.pop(excluir)
        print(f"O cadastro do aluno, foram excluidos")

def atualizarUsuarios(usuarios):
    buscar = input('E-mail do aluno: ')

    if usuarios == []:
        print("[Error]Nenhum aluno cadastrado")
    else:
        for usuario in usuarios:
            nome, email = usuario
            if email == buscar:
                print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')
                break

    atualizar = input("\nConfirmar a atualização de cadastro?[s/n]: ").lower()
    if atualizar in ['s', 'sim']:
        novoNome = input("Informe o nome atualizado: ").lower()
        nomeAtualizado = usuario.index(nome)
        nomeAtualizado.update(novoNome)
        print(f"Seu nome foi atualizado para {nomeAtualizado}".capitalize())

def back():
    while True:
        back = str(input('\nPRESSIONE "ENTER" PARA VOLTAR AO MENU'))
        if not back:
            return False

def menu(): 
    print("\n" + 23 * "_" + "MENU" + 23 * "_")
    print("[1] Para cadastrar um novo aluno")
    print("[2] Para exibir a lista de alunos(Por ordem de cadastro)")
    print("[3] Para exibir a lista de aluno(Por ordem Alfabética)")
    print("[4] Para buscar um aluno por email de cadastro")
    print("[5] Para remover o cadastro de um aluno")
    print("[6] Para atualizar o nome de um aluno")
    print("[7] Para encerrar o programa")
    print(50 * "_")

def main():
    usuarios = []

    while True:
        menu()
        opcao = int(input('\nQual a sua ação: '))
        if opcao == 1:
            cadastrarUsuarios(usuarios)
            back()
        elif opcao == 2:
            usuariosCadastrados(usuarios)
            back()
        elif opcao == 3:
            exibirOrdemAlfabetica(usuarios)
            back()
        elif opcao == 4:
            buscarUsuarioEmail(usuarios)
            back()
        elif opcao == 5:
            removerUsuarios(usuarios)
            back()
        elif opcao == 6:
            atualizarUsuarios(usuarios)
            back()
        elif opcao == 7:
            exit()
        else:
            print('Ação inválida')

if __name__ == "__main__":
    main()