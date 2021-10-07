
def cadastroUsuario(usuarios):
    qtdCadastro = int(input("Quantos usuarios deseja cadastrar? "))
    contador = 0
    while qtdCadastro != contador:
        nome = input("Digite o nome de usuário: ").lower()
        email = input("Digite o email: ").lower()
        usuarios.append((nome, email))

        contador += 1


def exibirOrdemAlfabetica(usuarios):

    if usuarios != []:
        usuariosOrdenadas = sorted(usuarios, key=len)
        print(usuariosOrdenadas)
    else:
        print("Não existe nenhum usuário cadastrado")

def usuariosCadastrados(usuarios):

    if usuarios != []:
        for usuario in usuarios:
            nome, email = usuario
            print(f'Nome: {nome}, Email: {email}'.capitalize())
    else:
        print("Não existe nenhum usuário cadastrado")


def buscarUsuarioNome(usuarios):
    buscar = input('Email do usuário: ')
    for usuario in usuarios:
        nome, email = usuario
        if email == buscar:
            print(f'O usuário foi encontrado como > Nome: {nome}, Email: {email}')
            break
    else:
        print(f'Usuario não encontrado')

def removerUsuario(usuarios):
    buscar = input('Email do usuário: ')

    if usuarios == []:
        print("Nenhum usuario cadastrado")
    else:
        for usuario in usuarios:
            nome, email = usuario
            if email == buscar:
                print(f'O usuário foi encontrado como > Nome: {nome}, Email: {email}')
                break     

    atualizar = input("Deseja remover o usuario?[s/n]: ").lower()

    if atualizar in ['s', 'sim']:
        excluir = usuarios.index(usuario)
        usuarios.pop(excluir)
        print(f"Seu usuario e E-mail, foram excluidos")

def atualizarUsuario(usuarios):
    buscar = input('Email do usuário: ')

    if usuarios == []:
        print("Nenhum usuario cadastrado")
    else:
        for usuario in usuarios:
            nome, email = usuario
            if email == buscar:
                print(f'O usuário foi encontrado como > Nome: {nome}, Email: {email}')
                break

    atualizar = input("Confirmimar a atualização?[s/n]: ").lower()
    if atualizar in ['s', 'sim']:
        novoNome = input("Informe o nome atualizado: ").lower()
        nomeAtualizado = usuario.index(nome)
        nomeAtualizado.update(novoNome)
        print(f"Seu nome foi atualizado para {nomeAtualizado}".capitalize())

def menu(): 
    print(23 * "_" + "MENU" + 23 * "_")
    print("Para cadastrar um novo usuario digite: 1")
    print("Para exibir a lista de usuarios digite: 2")
    print("Para exibir a lista de usuarios digite: 3")
    print("Buscar por um usuario digite: 4")
    print("Para remover um usuarios digite: 5")
    print("Para atualizar o nome de um usuarios digite: 6")
    print("Para encerrar o programa digite: 7")
    print(50 * "_")

def main():
    usuarios = []

    while True:
        menu()
        opcao = int(input('Qual a sua ação: '))
        if opcao == 1:
            cadastroUsuario(usuarios)
        elif opcao == 2:
            usuariosCadastrados(usuarios)
        elif opcao == 3:
            exibirOrdemAlfabetica(usuarios)
        elif opcao == 4:
            buscarUsuarioNome(usuarios)
        elif opcao == 5:
            removerUsuario(usuarios)
        elif opcao == 6:
            atualizarUsuario(usuarios)
        elif opcao == 7:
            exit()
        else:
            print('Ação inválida')

if __name__ == "__main__":
    main()