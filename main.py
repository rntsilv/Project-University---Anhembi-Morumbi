listaUsuarios = []

dicionarioCadastro={
    "nome": "", 
    "email": ""
    }

def buscarUsuarioNome():
    global buscarUsuario

    while True:
        buscarUsuario = input("Digite o nome do usuario: ").upper()

        if buscarUsuario in dicionarioCadastro['nome'] and buscarUsuario != "":
            print("Foi encontrado um usuario ja cadastrado com esse nome")
            return False
        elif buscarUsuario == "":
            print("Você deveria preencher o nome corretamente")
            continue
        else:
            print("Não foi encontrado nenhum usuário com o mesmo nome")
            while True:
                op = input("Deseja se cadastrar com esse nome?[s/n]: ").upper()
                if op in ['S', 'SIM']:
                    return buscarUsuario
                elif op in ['N', 'NAO', 'NO', 'NÃO']:
                    print("ok")
                    return False
                else:
                    print("Não entendi, pode repetir?")
                    continue


def cadastroUsuario():

    if buscarUsuarioNome() == False:
        while True:

            dicionarioCadastro["nome"] = input("Insira o nome completo: ").upper()
            dicionarioCadastro["email"] = input("Insira o e-mail: ").upper()                

            if dicionarioCadastro["nome"] != "" and dicionarioCadastro['email'] != "":
                print("\nUsuario cadastrado!\n")
                print("Nome: {}\nEmail: {}\n".format(dicionarioCadastro["nome"].capitalize(), dicionarioCadastro["email"].capitalize()))
                return False
            else:
                print("Você precisa digitar o nome e o e-mail corretamente")

    elif buscarUsuario != None:
        
        while True:
            dicionarioCadastro["nome"] = buscarUsuario
            dicionarioCadastro["email"] = input("Insira o e-mail: ").upper()                

            if dicionarioCadastro["nome"] != None and dicionarioCadastro['email'] != None:
                print("\nUsuario cadastrado!\n")
                print("Nome: {}\nEmail: {}\n".format(dicionarioCadastro["nome"].capitalize(), dicionarioCadastro["email"].capitalize()))
                return False
            else:
                print("Você precisa digitar o nome e o e-mail corretamente")

def opcaoCadastro():
    while True:
        qtdCadastro = int(input("Quantos usuarios deseja cadastrar? "))
        contador = 0
        if qtdCadastro in range(1, 10):
            while qtdCadastro != contador:
                novoUsuario = cadastroUsuario()
                listaUsuarios.append(novoUsuario) 
                contador += 1
                return False
        else:
            print("Você só pode cadastrar de 1 a 10 usários")
            continue

        
def exibirOrder():

    while True:
        opcao = input("Deseja exibir  a lista em ordem alfabetica?[s/n]: \n").upper()
        if opcao in ['S', 'SIM']:
            exibirOrdemAlfabetica()
        elif opcao in ['N', 'NAO', 'NO', 'NÃO']: 
            exibirLista()

def exibirOrdemAlfabetica():
    ordernarPorNome = "nome"
    valorDaChave = [nome[ordernarPorNome]for nome in listaUsuarios] 
    valorDaChave.sort()
    print(valorDaChave)
    
def exibirLista():
    
    ordernarPor = "nome"
    valorDaChave = [nome[ordernarPor] for nome in listaUsuarios]
    print(valorDaChave)

def exibirUsuario():
    buscarUsuario = input("Digite o nome do usuário: ").upper()

    if buscarUsuario in dicionarioCadastro['nome']:
        print(f"Usuario localizado: {dicionarioCadastro['nome'].capitalize()}")
    else:
        print('Não existe nenhum usuário com esse nome cadastrado atualmente')
        
def removerUsuario():
    buscarUsuario = input("Digite o e-mail do usuario: ").upper()
    for indice in listaUsuarios:
        if buscarUsuario == indice['email']:
            print("Usuarios loclizado {}".format(indice["nome"]))
            break
    confirmarRemoção=input("Deseja remover usuario?[s/n]: ").upper()
    if confirmarRemoção in ['S', 'SIM']:
        excluir = listaUsuarios.index(indice)
        listaUsuarios.pop(excluir)
        for  indice in listaUsuarios:
            verificador = True
            if buscarUsuario == indice['email']:
                verificador = False
                break
            if verificador == False:
                print("Usuario não localizado ")
                return
                
def atualizarUsuario():
    buscarUsuario = input("Digite o e-mail do usuario: ").upper()
    for  indice in listaUsuarios:
        if buscarUsuario == indice['email']:
            print("Usuarios loclizado {}".format(indice["nome"]))
            break
    atualizar=input("Confirmimar a atualização?[s/n]: ").upper()
    if atualizar in ['S','SIM']:
        novoNome = input("Informe o nome atualizado: ").upper
        indice.update({"nome":novoNome})
    elif atualizar in ['N', 'NAO', 'NO', 'NÃO']:
        return back()

def menu():
    acessoFunções={
    "1": opcaoCadastro,
    "2": exibirOrder,
    "3": exibirUsuario,
    "4": removerUsuario,
    "5": atualizarUsuario,
    
    }  

    print("___________________MENU___________________")
    print("Para cadastrar um novo usuario digite: 1")
    print("Para exibir a lista de usuarios digite: 2")
    print("Buscar por um usuario digite: 3")
    print("Para remover um usuarios digite: 4")
    print("Para atualizar o nome de um usuarios digite: 5")
    print("Para encerrar o programa digite: 6")
    print("__________________________________________")
    opcao = input("O que função deseja acessar? ")
    if opcao =="6":
        print("Encerrando o Programa")
        exit()
    case = acessoFunções.get(opcao)
    case()

def back():
    while True:
        op = input("Você deseja voltar ao Menu?[s/n]: ").upper()
        if op in ['S', 'SIM']:
            return False
        elif op in ['N', 'NAO', 'NO', 'NÃO']:
            print("Encerrando o programa")
            exit()
        else:
            print("Não entendi, pode repetir?")
            continue

        
def main():
    while True:
        menu()
        back()

if __name__ == "__main__":
    main()
    
    
    