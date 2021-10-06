listaUsuarios = []

def cadastroUsuario():
    nomeUsuario = input("Insira o nome completo: ").upper()
    emailUsuario = input("Insira o e-mail:  ").upper()

    dicionarioCadastro={"nome": nomeUsuario, "email": emailUsuario}
    print("\nUsuario cadastrado!\n")
    print("Nome: {}\nEmail: {}\n".format(nomeUsuario, emailUsuario) )
    return dicionarioCadastro
    
def opcaoCadastro():
        qtdCadastro = int(input("Quantos usuarios deseja cadastrar? "))
        contador = 0
        while qtdCadastro != contador:
            novoUsuario = cadastroUsuario()
            listaUsuarios.append(novoUsuario) 
            contador += 1
        
def exibirOrder():
 
    opcao = input("Deseja exibir  a lista em ordem alfabetica?\n").lower()
    if opcao == "sim":
        exibirOrdemAlfabetica()
    else: 
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
    print("Usuario localizado: ",buscarUsuarioNome())


def buscarUsuarioNome():
    buscarUsuario = input("Digite o nome do usuario: ").upper()

    for  indice in listaUsuarios:
        if buscarUsuario == indice['nome']:
           return indice['nome']
           
def removerUsuario():
    buscarUsuario = input("Digite o e-mail do usuario: ").upper()
    for  indice in listaUsuarios:
        if buscarUsuario == indice['email']:
            print("Usuarios loclizado {}".format(indice["nome"]))
            break
    confirmarRemoção=input("Deseja remover usuario? ").lower()
    if confirmarRemoção =="sim":
        excluir = listaUsuarios.index(indice)
        listaUsuarios.pop(excluir)
        for  indice in listaUsuarios:
            verificador = True
            if buscarUsuario == indice['email']:
                verificador = False
                break
            if verificador == False:
                print("Usuario não localizado ")
                
def atualizarUsuario():
    buscarUsuario = input("Digite o e-mail do usuario: ").upper()
    for  indice in listaUsuarios:
        if buscarUsuario == indice['email']:
            print("Usuarios loclizado {}".format(indice["nome"]))
            break
    atualizar=input("Confirmimar a atualização?\nSim - Não\n> ").lower()
    if atualizar == "sim":
        novoNome = input("Informe o nome atualizado: ").upper
        indice.update({"nome":novoNome})
                
def menu():
    acessoFunções={
    "1": opcaoCadastro,
    "2": exibirOrder,
    "3": exibirUsuario,
    "4": removerUsuario,
    "5": atualizarUsuario,
    
    }  
    while True:
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
            break
        case = acessoFunções.get(opcao)
        case()
        
def main():
    menu()

if __name__ == "__main__":
    main()
    
    
    