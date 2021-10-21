from string import ascii_letters, digits
import random

MAX_RANGE = 8
MIN_RANGE = 4

def encrypt(sequence):

    if len(sequence) < MIN_RANGE:
        print('Você não pode criptografar senhas menores que 4 digitos')
    elif len(sequence) > MAX_RANGE:
        print('Você não pode criptografar senhas maiores que 8 digitos')
    else:
        cifra = ''
        caracteres = ascii_letters + digits
        chave = random.choice(range(126)) #gera numeros aleatoriamente até 126 hur dar

        for letra in sequence:
            if letra in caracteres: #verifica se a variavel letra esta entre as 62 letras do caracteres
                posicao = caracteres.find(letra) #voce ja deve saber oque isso faz então fds(pega a posição da letra no caracteres em numero)
                posicao = (posicao + chave) % 62 #posição += chave que é numeros aleatorios e usamos a aritmética modular no limite de 62
                #pq 62 o lucas perguntaria e eu digo que é pq somei todas as letras maiusculas e minusculas, mais os numero de (0, 9), então ao todo deu 62 bruh
                cifra = cifra + caracteres[posicao] #cifra recebe o resultado passado, mais o caracteres[numero] porra
                
        return print(cifra)

mensagem = input(': ')

encrypt(mensagem)