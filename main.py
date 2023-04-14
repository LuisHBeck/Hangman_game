import defs_

def main():
    print('SEJA BEM-VINDO(A) AO JOGO DA FORCA')
    modo = defs_.modo_de_jogo()

    if modo == 'Nutella':
        import nutella
        nutella.rodar_nutella()
    elif modo == 'Café com leite':
        import cafe_com_leite
        cafe_com_leite.rodar_cafe_com_leite()
    elif modo == 'Raiz':
        import raiz
        raiz.rodar_raiz()

if __name__ == '__main__':
    main()
