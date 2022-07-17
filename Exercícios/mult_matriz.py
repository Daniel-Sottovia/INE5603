def inputMatriz(qtLinhas):
    r = []
    for l in range(qtLinhas):
        r.append([int(ent) for ent in input().split()])
    return r


def linhas():
    num = int(input())
    return num


def montar_matriz():
    pri_tam = linhas()
    pri_matriz = inputMatriz(pri_tam)
    sec_tam = linhas()
    sec_matriz = inputMatriz(sec_tam)
    if not checar_numerica(pri_matriz) or not checar_numerica(sec_matriz):
        return print(0)
    if not checar_m_n(pri_matriz, sec_matriz):
        return print(-1)

    final = multiplicacao(pri_matriz, sec_matriz)
    return imprimir(final)



def checar_numerica(matriz):
    tam = len(matriz)
    coluna = len(matriz[0])
    cont = 0
    while cont < tam:
        cont_c = len(matriz[cont])
        if cont_c != coluna:
            return False
        cont += 1
    return True


def checar_m_n(pri_matriz, sec_matriz):
    pri_col = len(pri_matriz[0])
    sec_matriz = len(sec_matriz)
    if pri_col == sec_matriz:
        return True
    else:
        return False


def colunaEmlinha(matriz, coluna):
    final = []
    tam = len(matriz)
    cont = 0
    while cont < tam:
        final.append(matriz[cont][coluna])
        cont += 1
    return final

def multiplicacao_de_linhas(pri_matriz, sec_matriz):
    tam = len(pri_matriz)
    soma = 0
    cont = 0
    while cont < tam:
        soma = soma + pri_matriz[cont]*sec_matriz[cont]
        cont += 1
    return soma

def multiplicacao(pri_matriz, sec_matriz):
    linha = len(pri_matriz)
    coluna = len(sec_matriz[0])
    cont_l = 0
    final = []
    while cont_l < linha:
        final.append([])
        cont_c = 0
        while cont_c < coluna:
            linearizado_sec = colunaEmlinha(sec_matriz,cont_c)
            soma = multiplicacao_de_linhas(pri_matriz[cont_l],linearizado_sec)
            final[cont_l].append(soma)
            cont_c += 1
        cont_l += 1
    return final




def imprimir(matriz):
    tam = len(matriz)
    cont_l = 0
    while cont_l < tam:
        cont_c = 0
        coluna = len(matriz[cont_l])
        while cont_c < coluna:
            print(f'{matriz[cont_l][cont_c]}', end=' ')
            cont_c += 1
        cont_l += 1
        print()

montar_matriz()