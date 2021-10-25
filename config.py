from string import ascii_letters, digits, punctuation
import files, console


defaultLogin = "admin"
defaultPassword = "admin1234"


MAX_RANGE = 8
MIN_RANGE = 4
CARACTERES = ascii_letters + digits + punctuation
CHAVE = 140 #idade do retalio uwu


def encrypt(sequence):
    global CHAVE
    arfic = ''

    for letra in sequence:
        if letra in CARACTERES:
            posicao = CARACTERES.find(letra)
            posicao = (posicao + CHAVE) % 94
            arfic = arfic + CARACTERES[posicao]
                
    return arfic


def decrypt(sequence):
    global CHAVE
    CHAVE = len(CARACTERES) - CHAVE
    return encrypt(sequence)


def verifyLogin(login, senha):
    
    if login in files.getFileContents("login") and senha in files.getFileContents("senha"):
        return True
    else:
        return False


def loginAdm():
    while True:
        print("Bem-vindo, acesse com seu login de administrador\n")
        userName = input("Username: ")
        password = input("Password: ")

        if verifyLogin(userName, password) == True:
            print()
            console.animated("Concedendo acesso")
            break
        else:
            print("\n[Erro] Usuário ou senha incorretos, tente novamente.")
            continue