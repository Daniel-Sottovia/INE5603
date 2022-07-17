import random


def exercicio_01(linha,coluna):
    matriz = []
    cont_l = 0
    while cont_l < linha:
        cont_c = 0
        matriz.append([])
        while cont_c < coluna:
            matriz[cont_l].append(0)
            cont_c += 1
        cont_l += 1
    return matriz

#print(exercicio_01(linha=3,coluna=4))

def exercicio_02(linha,coluna,limite):
    matriz = []
    cont_l = 0
    while cont_l < linha:
        cont_c = 0
        matriz.append([])
        while cont_c < coluna:
            matriz[cont_l].append(random.uniform(limite,-limite))
            cont_c += 1
        cont_l += 1
    return matriz

#print(exercicio_02(2,3,2))

def exercicio_03(matriz):
    final = []
    linha = len(matriz)
    final.append(linha)
    analise = []
    cont_l = 0
    while cont_l < linha:
        tam = len(matriz[cont_l])
        analise.append(tam)
        cont_l += 1
    coluna = len(analise)
    cont_c = 0
    est = 0
    while cont_c < coluna:
        if analise[0] != analise[cont_c]:
            est += 1
        cont_c += 1
    if est > 0 :
        final.append([])
    else:
        final.append(analise[0])
    return final

#linda = [[2,-1], [3,5], [0,9]]
#print(exercicio_03(linda))

def iguais(matriz, linda):
    if len(matriz) != len(linda):
        return False
    tam = len(matriz)
    cont = 0
    coluna_01 = []
    coluna_02 = []
    while cont < tam:
        coluna_01.append(len(matriz[cont]))
        coluna_02.append(len(linda[cont]))
        cont += 1
    if coluna_01 != coluna_02:
        return False
    return True

#matriz = [[2,1,3],[5,6],[9]]
#linda = [[2,1,3],[5,6],[9]]
#print(iguais(matriz=matriz,linda=linda))

def exercicio_04(matriz, linda):
    if iguais(matriz=matriz,linda=linda):
        final = []
        linha = len(matriz)
        cont_l = 0
        while cont_l < linha:
            coluna = len(matriz[cont_l])
            cont_c = 0
            final.append([])
            while cont_c < coluna:
                soma = matriz[cont_l][cont_c] + linda[cont_l][cont_c]
                final[cont_l].append(soma)
                cont_c += 1
            cont_l += 1
        return final
    else:
        return 'Não é possível realizar soma das matrizes.'

#matriz = [[2,1,3],[5,6,2],[9]]
#linda = [[2,1,3],[5,6,1],[9]]
#print(exercicio_04(matriz=matriz,linda=linda))

def exercicio_05(linda):
    linha = len(linda)
    cont_l = 0
    final = []
    while cont_l < linha:
        coluna = len(linda[cont_l])
        cont_c = 0
        final.append([])
        while cont_c < coluna:
            if cont_l != cont_c:
                adic = linda[cont_l][cont_c] * 10
                final[cont_l].append(adic)
            else:
                final[cont_l].append(0)
            cont_c += 1
        cont_l += 1

    return final

#matriz = [[1,4,5],[-2,3,6],[8,-1,9]]
#print(exercicio_05(matriz))

def fatorial(num):
    prod = 1
    while num > 0:
        prod = prod * num
        num = num - 1
    return prod


def exercicio_06(linda):
    linha = len(linda)
    cont_l = 0
    final = []
    while cont_l < linha:
        cont_c = 0
        final.append([])
        while cont_c < 3:
            if cont_c == 0:
                prod = 10 * linda[cont_l][cont_c]
                final[cont_l].append(prod)
            elif cont_c == 1:
                num = fatorial(linda[cont_l][cont_c])
                final[cont_l].append(num)
            else:
                modulo = abs(linda[cont_l][cont_c])
                final[cont_l].append(modulo)
            cont_c += 1
        cont_l += 1
    return final

#matriz = [[1,2,-3],[4,5,-6],[7,8,9],[10,11,12]]
#print(exercicio_06(linda=matriz))

from Exercícios.arquivo import quadrada

def exercicio_07(matriz):
    if quadrada(matriz):
        tam = len(matriz)
        cont_l = 0
        final = [[],[]]
        while cont_l < tam:
            maior = matriz[cont_l][0]
            menor = matriz[cont_l][0]
            cont_c = 0
            while cont_c < tam:
                if maior < matriz[cont_l][cont_c]:
                    maior = matriz[cont_l][cont_c]
                elif menor > matriz[cont_l][cont_c]:
                    menor = matriz[cont_l][cont_c]
                if cont_c == tam - 1:
                    final[0].append(maior)
                    final[1].append(menor)
                cont_c += 1
            cont_l += 1
        return final
    else:
        return 'Não é matriz quadrada.'

#linda = [[3,4,2],[-1,-2,-3],[5,6,7]]
#print(exercicio_07(linda))

def exercicio_08(matriz):
    final = []
    tam = len(matriz)
    cont_l = 0
    while cont_l < tam:
        final.append([])
        cont_c = 0
        while cont_c < tam:
            valor = matriz[cont_l][cont_c] * matriz[cont_l][tam - 1 - cont_l]
            final[cont_l].append(valor)
            cont_c += 1
        cont_l += 1
    return final

#linda = [[1,2,3],[2,4,6],[5,7,11]]
#print(exercicio_08(linda))