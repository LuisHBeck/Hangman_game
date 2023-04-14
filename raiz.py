import requests
from GAME_FORCA.testes import defs_
from xml.dom import minidom

collors = {
    'X': '\33[7;32m',
    'Y': '\33[4;35m',
    'Z': '\33[7;34m',
    'N': '\33[7;31m',
    'C': '\33[m'
}

dicas = []
palavras = []
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
letras_erradas = []
letras_certas = []

PROXIES = {
    'http': 'http://ct67ca:23%23INDUSTRIAdigital@proxy.br.bosch.com:8080',
    'https': 'http://ct67ca:23%23INDUSTRIAdigital@proxy.br.bosch.com:8080'
}

while len(dicas) != 1:
    try:
        url1 = 'http://api.dicionario-aberto.net/random'
        response1 = requests.get(url1)
        palavra_sorteada1 = response1.json()['word']

        url = f"http://api.dicionario-aberto.net/word/{palavra_sorteada1}"
        response2 = requests.get(url)
        definition = response2.json()[0]["xml"]

        parsedXML = minidom.parseString(definition)
        elements = parsedXML.getElementsByTagName('def')

        for element in elements:
            locations = element.firstChild.nodeValue

        locations_corrigido = str(locations).strip().replace('\n', ' ')

        dicas.append(locations_corrigido)

        palavra_sorteada1 = palavra_sorteada1.upper()

        if len(dicas) == 1:
            palavras.append(palavra_sorteada1)

    except KeyError:
        continue

print(palavra_sorteada1)
palavra_secreta = ["_"] * len(palavras[0])

defs_.cabecalho("\t\t{}JOGO DA FORCA{}\t\t".format(collors['Z'], collors['C']))
def rodar_raiz():
    defs_.comecar(palavra_sorteada1, 30)
    defs_.dica_palavra(dicas, 0)
    while True:
        if len(vidas1) == 0:
            print(personagem[0])
            defs_.fim(palavra_sorteada1, "{}{}{}".format(collors['N'], "VOCÊ PERDEU!", collors['C']))
            defs_.palavra_fim(palavra_sorteada1)
            quit()
        if len(vidas1) == 0:
            defs_.finalizar()
        defs_.jogo_inicio(vidas1)
        print(personagem[len(vidas1)], end='  ')
        print(" ".join(palavra_secreta).strip())
        print()
        tentativa_letra = defs_.entrada_letra()
        defs_.letra_certa(tentativa_letra, palavra_sorteada1, letras_certas, palavra_secreta)
        defs_.letra_errada(tentativa_letra, letras_erradas, palavra_sorteada1, vidas1)
        defs_.espaco()
        defs_.vitoria(palavra_secreta, vidas1, palavra_sorteada1)

rodar_raiz()
