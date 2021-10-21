from string import ascii_letters, digits, punctuation

MAX_RANGE = 8
MIN_RANGE = 4
CARACTERES = ascii_letters + digits + punctuation
CHAVE = 126 #idade do retalio uwu



def encrypt(sequence):
    global CHAVE
    arfic = ''

    for letra in sequence:
        if letra in CARACTERES:
            posicao = CARACTERES.find(letra)
            posicao = (posicao + CHAVE) % 94
            arfic = arfic + CARACTERES[posicao]
                
    return arfic

def descrypt(sequence):
    global CHAVE
    CHAVE = len(CARACTERES) - CHAVE
    return encrypt(sequence)

mensagem = input(': ')

arfic = encrypt(mensagem)
cifra = descrypt(arfic)

print(f'{cifra.title()} : {arfic.title()}')
