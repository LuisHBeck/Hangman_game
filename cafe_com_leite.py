from GAME_FORCA.testes import defs_

collors = {
    'X': '\33[7;32m',
    'Y': '\33[4;35m',
    'Z': '\33[7;34m',
    'N': '\33[7;31m',
    'C': '\33[m'
}

# LISTAS UTILIZADAS
palavras = ["DUPLEX", "PIZZAIOLO", "LHAMA"]
dicas = ["Apartamento de dois andares", "Profissional especializado em pizzas", "Animal da família dos camelídeos"]
dicas2 = []
letras_erradas = []
letras_certas = []
vidas1 = ["❤", "❤", "❤", "❤", "❤", "❤"]
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

vidas = 6

defs_.cabecalho("\t\t{}JOGO DA FORCA{}\t\t".format(collors['Z'], collors['C']))

defs_.adicionar_palavras(palavras, dicas, vidas1)

num_palavra = defs_.sortear_palavra(palavras)
palavra_sorteada = palavras[num_palavra]
palavra_secreta = ["_"] * len(palavra_sorteada)

def rodar_cafe_com_leite():
    defs_.comecar(palavra_sorteada, 30)
    defs_.dica_palavra(dicas, num_palavra)
    while True:
        if len(vidas1) == 0:
            print(personagem[0])
            defs_.fim(palavra_sorteada, "{}{}{}".format(collors['N'], "VOCÊ PERDEU!", collors['C']))
            defs_.palavra_fim(palavra_sorteada)
            quit()
            defs_.finalizar()
        defs_.jogo_inicio(vidas1)
        print(personagem[len(vidas1)], end='  ')
        print(" ".join(palavra_secreta).strip())
        print()
        tentativa_letra = defs_.entrada_letra()
        defs_.letra_certa(tentativa_letra, palavra_sorteada, letras_certas, palavra_secreta)
        defs_.letra_errada(tentativa_letra, letras_erradas, palavra_sorteada, vidas1)
        defs_.espaco()
        defs_.vitoria(palavra_secreta, vidas1, palavra_sorteada)

rodar_cafe_com_leite()
