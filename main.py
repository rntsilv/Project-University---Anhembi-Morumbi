
def cadastroAluno(alunos):
    qtdCadastro = int(input("Quantos alunos deseja cadastrar? "))
    contador = 0
    while qtdCadastro != contador:
        nome = input("Digite o nome do aluno: ").lower()
        email = input("Digite o e-mail do aluno: ").lower()
        alunos.append((nome, email))

        contador += 1


def exibirOrdemAlfabetica(alunos):

    if alunos != []:
        alunosOrdenados = sorted(alunos, key=len)
        print(alunosOrdenados)
    else:
        print("Não existe nenhum aluno cadastrado")

def alunosCadastrados(alunos):

    if alunos != []:
        for aluno in alunos:
            nome, email = aluno
            print(f'Nome: {nome}, E-mail: {email}'.capitalize())
    else:
        print("Não existe nenhum aluno cadastrado")


def buscarUsuarioNome(alunos):
    buscar = input('E-mail do aluno: ')
    for aluno in alunos:
        nome, email = aluno
        if email == buscar:
            print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')
            break
    else:
        print(f'Aluno não encontrado')

def removerAluno(alunos):
    buscar = input('E-mail do aluno: ')

    if alunos == []:
        print("Nenhum aluno cadastrado")
    else:
        for aluno in alunos:
            nome, email = aluno
            if email == buscar:
                print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')
                break     

    atualizar = input("Deseja remover o cadastro do aluno?[s/n]: ").lower()

    if atualizar in ['s', 'sim']:
        excluir = alunos.index(aluno)
        alunos.pop(excluir)
        print(f"O aluno e e-mail, foram excluidos do cadastro")

def atualizarAluno(alunos):
    buscar = input('E-mail do aluno: ')

    if alunos == []:
        print("Nenhum aluno cadastrado")
    else:
        for aluno in alunos:
            nome, email = aluno
            if email == buscar:
                print(f'O aluno foi encontrado como > Nome: {nome}, E-mail: {email}')
                break

    atualizar = input("Confirmimar a atualização de cadastro?[s/n]: ").lower()
    if atualizar in ['s', 'sim']:
        novoNome = input("Informe o nome atualizado: ").lower()
        nomeAtualizado = aluno.index(nome)
        nomeAtualizado.update(novoNome)
        print(f"Seu nome foi atualizado para {nomeAtualizado}".capitalize())

def menu(): 
    print(23 * "_" + "MENU" + 23 * "_")
    print("[1] Para cadastrar um novo aluno")
    print("[2] Para exibir a lista de alunos")
    print("[3] Para buscar por um aluno")
    print("[4] Para remover um aluno")
    print("[5] Para atualizar o nome de um aluno")
    print("[6] Para encerrar o programa")
    print(50 * "_")

def main():
    alunos = []

    while True:
        menu()
        opcao = int(input('Qual a sua ação: '))
        if opcao == 1:
            cadastroAluno(alunos)
        elif opcao == 2:
            alunosCadastrados(alunos)
        elif opcao == 3:
            exibirOrdemAlfabetica(alunos)
        elif opcao == 4:
            buscarUsuarioNome(alunos)
        elif opcao == 5:
            removerAluno(alunos)
        elif opcao == 6:
            atualizarAluno(alunos)
        elif opcao == 7:
            exit()
        else:
            print('Ação inválida')

if __name__ == "__main__":
    main()