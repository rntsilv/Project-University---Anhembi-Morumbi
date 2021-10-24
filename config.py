from string import ascii_letters, digits, punctuation
import time, sys


defaultLogin = "admin"
defaultPassword = "admin1234"


MAX_RANGE = 8
MIN_RANGE = 4
CARACTERES = ascii_letters + digits + punctuation
CHAVE = 140 #idade do retalio uwu


def inputFile(filename, newValue):
    with open(f"txtSrc/{filename}.txt", mode="w", encoding="utf-8") as file:
        file.write(newValue)


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


def loginAdm():
    while True:
        print("Bem-vindo, acesse com seu login de administrador\n")
        userName = input("Username: ")
        password = input("Password: ")

        login = userName.lower() + password

        if login == querryLogin():
            print()
            animated("Concedendo acesso")
            break
        else:
            print("\n[Erro] Usuário ou senha incorretos, tente novamente.")
            continue


def pressCommand():
    while True:
        pressCommand = str(input('\nPRESSIONE "ENTER" PARA CONTINUAR'))
        if not pressCommand:
            break

def animated(loading):
    chars = "|/—\|/—\|" 
    for char in chars:
        sys.stdout.write("\r" + loading + " " + char)
        time.sleep(0.3)
        sys.stdout.flush()
