def exercicio_01():
    entrada = int(input('Entrada: '))
    linhas = 0
    colunas = 0
    cont = 0
    controle = 0
    while linhas >= 0:
        num = 1
        while colunas < controle:
            print(f'{num}', end='')
            num += 1
            colunas += 1
        colunas = 0
        print('\n')
        if cont < entrada:
            linhas += 1
            if controle == 0:
                controle += 1
            else:
                controle += 2
        else:
            linhas = linhas - 1
            if controle == 1:
                controle = controle - 1
            else:
                controle = controle - 2
        cont += 1

#exercicio_01()

#def exercicio_02():

#def exercicio_03(linda):

def exercicio():
    linhas = int(input('Entrada: '))
    colunas = linhas
    cont_linha = 0
    n = 1
    while cont_linha < linhas:
        cont_col = 0
        num = n
        rep = n
        while cont_col < colunas:
            print(f'{num}',end='')
            if rep > 1:
                rep = rep - 1
            else:
                if num < colunas:
                    num += 1
            cont_col += 1
        print('')
        cont_linha += 1
        n += 1

exercicio()
        