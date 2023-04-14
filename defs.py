from random import randint
import os
from threading import Timer

collors = {
    'X': '\33[7;32m',
    'Y': '\33[4;35m',
    'Z': '\33[7;34m',
    'N': '\33[7;31m',
    'C': '\33[m'
}

personagem = [
    '''
 _____________
|             |
|             |
|             0
|            /|\⠀⠀
|             | 
|            / \⠀
|
|
''',
    '''
 _____________
|             |
|             |
|             0
|            /|\⠀⠀
|             | 
|            /
|
|
''',
    '''
 _____________
|             |
|             |
|             0
|            /|\⠀⠀
|             | 
|             
|
|
''',
    '''
 _____________
|             |
|             |
|             0
|            /|
|             |
|             
|
|
''',
    '''
 _____________
|             |
|             |
|             0
|             |
|             |
|
|
|
''',
    '''
 _____________
|             |
|             |
|             0
|
|
|
|
|
    ''',
    '''
 _____________
|             |
|             |
|
|
|
|
|
|
'''
]

def cabecalho(msg):
    espaco()
    print("{: ^30}".format("\t\t{}JOGO DA FORCA{}\t".format(collors['Z'], collors['C'])))
    espaco()


def espaco():
    print("—"*30)


def sortear_palavra(palavras):
    pos_palavra = randint(0, (len(palavras) - 1))
    return pos_palavra


def dica_palavra(dicas, num_palavra):
    print("{:—^30}".format(" DICA "))
    print("{}{: ^30}{}".format(collors['X'], dicas[num_palavra], collors['C']))
    print("—"*30)


def dica_palavra2(vidas1, dicas2, num_palavra):
    if len(vidas1) == 3:
        print("{:—^30}".format(" DICA 2 "))
        print("{}{: ^30}{}".format(collors['X'], dicas2[num_palavra], collors['C']))
        print("—" * 30)


def jogo_inicio(vidas1):
    print("Vidas: ", end='')
    for c in range(len(vidas1)):
        print(vidas1[c], end=" ")
    print()


def entrada_letra():
    teste = True
    while teste:
        input_letra = str(input("Digite uma letra: ")).upper()
        if input_letra.isnumeric() or input_letra.isspace() or len(input_letra) == 0:
            print()
            print('Tentativa inválida! Tente outra vez.')
        else:
            return input_letra


def letra_certa(tentativa_letra, palavra_sorteada, letras_certas, palavra_secreta):
    while len(tentativa_letra) > 1:
        print("Digite apenas uma letra!")
        print()
        tentativa_letra = str(input("Digite uma letra: ")).upper().strip()

    if tentativa_letra in palavra_sorteada:
        if tentativa_letra in letras_certas and tentativa_letra not in " ":
            print("Você já digitou essa letra. Tente uma novak.")
        else:
            letras_certas.append(tentativa_letra)
            for letra in range(len(palavra_sorteada)):
                if palavra_sorteada[letra] == tentativa_letra:
                    palavra_secreta[letra] = tentativa_letra
                    print("{}{}{}".format(collors['X'], "ACERTOU A LETRA", collors['C']))
    else:
        if tentativa_letra not in letras_certas:
            print("{}{}{}".format(collors['N'], "ERROU A LETRA", collors['C']))


def letra_errada(tentativa_letra, letras_erradas, palavra_sorteada, vidas1):
    if tentativa_letra not in letras_erradas and len(tentativa_letra) == 1:
        if tentativa_letra not in palavra_sorteada:
            vidas1.pop()
            letras_erradas.append(tentativa_letra)
            print(personagem[len(vidas1)])
            print("Tentativas erradas: {}".format(letras_erradas))
    else:
        print("Você já digitou essa letra. Tente uma nova.")



def finalizar_jogo(personagem, modo_de_jogo):
    if modo_de_jogo == "Café com leite":
        palavra_fim("FIM")
    quit()


def adicionar_palavras(palavras, dicas, vidas1):
    global adicionar_qnt, vidas
    adicionar = " "
    while adicionar not in "SN":
        print("QUANTIDADE DE PALVRAS ADICIONADAS SERÁ DESCONTADAS DE SUA VIDA")
        adicionar = input("Você deseja adicionar palavras? [S/N]: ").upper()
        if adicionar.isnumeric():
            while adicionar.isnumeric():
                print("Opção inválida! Tente novamnete")
                adicionar = input("Você deseja adicionar palavras? [S/N]: ").upper()

    if adicionar == "S":
        adicionar_qnt = 3

        while adicionar_qnt > 2:
            adicionar_qnt = int(input('''
        [1] - uma palavra
        [2] - duas palavras
        >> '''))
            if adicionar_qnt <= 2:
                break

        for c in range(0, adicionar_qnt):
            palavras.append(input("Digite sua palavra: ").upper())
            dicas.append(input("Digite sua dica: "))
            del vidas1[-1]



def remover_palavras(palavras, dicas, vidas1):
    global vidas
    remover = " "
    while remover not in "SN":
        print("QUANTIDADE DE PALVRAS REMOVIDAS SERÁ DESCONTADAS DE SUA VIDA")
        remover = input("Você deseja remover palavras? [S/N]: ").upper()
        if remover.isnumeric():
            while remover.isnumeric():
                print("Opção inválida! Tente novamnete")
                remover = input("Você deseja remover palavras? [S/N]: ").upper()

    if remover == "S":
        remover_qnt = 3

        while remover_qnt > 2:
            remover_qnt = int(input('''
        [1] - uma palavra
        [2] - duas palavras
        >> '''))
            if remover_qnt <= 2:
                break

        for c in range(0, remover_qnt):
            t = len(palavras)
            n = int(input("Digite a posição de {} a {}: ".format(0, t)))
            del palavras[n]
            del dicas[n]
            del vidas1[-1]
            vidas -= 1


def fim(palavra_sorteada, msg="{}{}{}".format(collors['N'], "VOCÊ PERDEU!", collors['C'])):
    espaco()
    print("{}{}{}".format(collors['Z'], "FIM DE JOGO!!!", collors['C']))
    print(msg)
    print("PALAVRA = {}{}{}".format(collors['Y'], palavra_sorteada, collors['C']))
    finalizar()


def vitoria(palavra_secreta, vidas1, palavra_sorteada):
    if "_" not in palavra_secreta:
        espaco()
        print(personagem[len(vidas1)])
        fim(palavra_sorteada, msg="{}{}{}".format(collors['N'], "VOCÊ GANHOU!", collors['C']))
        palavra_fim(palavra_sorteada)
        quit()
        finalizar()

def palavra_fim(palavra_sorteada):
    def temponeg(msg="\nSEU TEMPO ACABOU!!"):
        print(msg)
        print("PALAVRA = {}{}{}".format(collors['Y'], palavra_sorteada, collors['C']))
        pid = os.getpid()
        os.kill(pid, -1)
    return temponeg

def finalizar():
    pid = os.getpid()
    os.kill(pid, -1)


def comecar(palavra_sorteada, tempo=0):
    pronto = int(input('[1] PARA COMEÇAR: '))
    print('~~'*15)
    while pronto != 1:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
        pronto = int(input('[1] PARA COMEÇAR: '))
        print('~~' * 15)
    if pronto == 1:
        t = Timer(tempo, palavra_fim(palavra_sorteada))
        t.start()

def modo_de_jogo():
    import inquirer
    questions = [
        inquirer.List('modo',
                        message="Escolha o modo de jogo",
                        choices=['Nutella', 'Café com leite', 'Raiz'],
                        ),
        ]
    answers = inquirer.prompt(questions)
    return answers['modo']
