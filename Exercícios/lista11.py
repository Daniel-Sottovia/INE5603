#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:26:18 2022

@author: 18104319
"""

'''matriz = [[3,8],
          [1,-4,2],
          [-3, 7],
          [1],
          [5,2,9,11]]'''


def exercicio_01(matriz):
    n_linhas = len(matriz)
    cont_l = 0
    soma = 0
    while cont_l < n_linhas:
        n_col = len(matriz[cont_l])
        cont_c = 0
        while cont_c < n_col:
            soma = soma + matriz[cont_l][cont_c]
            cont_c += 1
        cont_l += 1
        
    print(f'{soma}')
    
#matriz = [[2,3],[1,5]]
#exercicio_01(matriz)
#matriz = [[3,8],[1,-4,2],[-3, 7],[1],[5,2,9,11]]
#exercicio_01(matriz)
    
def exercicio_02(matriz):
    n_linhas = len(matriz)
    cont_l = 0
    while cont_l < n_linhas:
        n_col = len(matriz[cont_l])
        cont_c = 0
        while cont_c < n_col:
            print(f'{matriz[cont_l][cont_c]}', end = ' ')
            cont_c += 1
        print()
        cont_l += 1
    
#matriz = [[1,2,3],[4,5],[6]]
#exercicio_02(matriz)

def exercicio_03(matriz):
    n_linhas = len(matriz)
    cont_l = 0
    maior = 0
    texto = 0
    while cont_l < n_linhas:
        n_col = len(matriz[cont_l])
        cont_c = 0
        while cont_c < n_col:
            if cont_l == 0 and cont_c == 0:
                maior = len(matriz[cont_l][cont_c])
                texto = matriz[cont_l][cont_c]
            elif len(matriz[cont_l][cont_c]) > maior:
                maior = len(matriz[cont_l][cont_c]) 
                texto = matriz[cont_l][cont_c]
            cont_c += 1
        cont_l += 1
    return print(f'Maior: {maior}\n Texto: {texto}')
        
        
#linda = [['a vida é bela','viaja'], ['saudades dela','olhares','olhos castanhos'], ['coracao sofre','nao se desgrudam']]
#exercicio_03(linda)

def exercicio_04(matriz):
    n_linhas = len(matriz)
    cont_l = 0
    maior = 0
    posicao = [0,0]
    while cont_l < n_linhas:
        n_col = len(matriz[cont_l])
        cont_c = 0
        while cont_c < n_col:
            if cont_l == 0 and cont_c == 0:
                maior = matriz[cont_l][cont_c]
                posicao[0] = cont_l
                posicao[1] = cont_c
            elif matriz[cont_l][cont_c] > maior:
                maior = matriz[cont_l][cont_c]
                posicao[0] = cont_l
                posicao[1] = cont_c
            cont_c += 1
        cont_l += 1
    return print(f'Maior: {maior}\n L:{posicao[0]} C:{posicao[1]}')

#matriz = [[3,8],[1,-4,2],[-3, 7],[1],[5,2,9,11]]
#exercicio_04(matriz)

def primo(num):
    cont = 0
    n = 1
    while n <= num:
        if num % n == 0:
            cont += 1
        n += 1
    if cont == 2:
        return True
    else:
        return False


def exercicio_05(matriz):
    n_linhas = len(matriz)
    cont_l = 0
    n_primo = 0
    while cont_l < n_linhas:
        n_col = len(matriz[cont_l])
        cont_c = 0
        while cont_c < n_col:
            if primo(matriz[cont_l][cont_c]):
                n_primo += 1
            cont_c += 1
        cont_l += 1
    return print(f'Temos {n_primo} elementos primos.')

#matriz=[[2,4,6],[17,8],[9,1]]
#exercicio_05(matriz)

def exercicio_06(matriz,num):
    n_linhas = len(matriz)
    cont_l = 0
    while cont_l < n_linhas:
        n_col = len(matriz[cont_l])
        cont_c = 0
        while cont_c < n_col:
            if matriz[cont_l][cont_c] == num:
                return True
            cont_c += 1
        cont_l += 1
    return False

#matriz = ([0, -2, 4],[2,1,9],[3,1,-3],[6,3,2])
#num = 2
#print(exercicio_06(matriz, num))

def exercicio_07(matriz):
    n_linhas = len(matriz)
    cont_l = 0
    while cont_l < n_linhas:
        n_col = len(matriz[cont_l])
        if n_linhas != n_col:
            return False
        cont_l += 1
    return True

#matriz = [[1,2],[4,5]]
#print(exercicio_07(matriz))

def exercicio_08(matriz):
    if not exercicio_07(matriz):
        return print('Não é uma matriz quadrada.')
    n_linhas = len(matriz)
    cont_l = 0
    final = []
    while cont_l < n_linhas:
        n_col = len(matriz[cont_l])
        cont_c = 0
        soma = 0
        while cont_c < n_col:
            soma = soma + matriz[cont_l][cont_c]
            cont_c += 1
        final.append(soma)
        cont_l += 1
    return final

#matriz = [[2,3,4],[1,1,1],[7,1,4]]
#print(exercicio_08(matriz))

def exercicio_09(matriz):
    linha = len(matriz)
    cl = 0
    nulos = []
    while cl < linha:
        coluna = len(matriz[cl])
        cc = 0
        while cc < coluna:
            if matriz[cl][cc] == '':
                nulos.append([cl,cc])
            cc += 1
        cl += 1
    return nulos

'''matriz = [['saudades', '', 'linda'],
          ['surfe', 'praia', 'areia'],
          ['olhar', 'castanho', 'pausa'],
          ['chorar'],
          ['', 'viver']]'''

#print(exercicio_09(matriz))

def linha_neg(matriz):
    linha = len(matriz)
    cl = 0
    final = []
    while cl < linha:
        coluna = len(matriz[cl])
        cc = 0
        neg_col = 0
        while cc < coluna:
            if matriz[cl][cc] < 0:
                neg_col += 1
            cc += 1
            
        if neg_col == cc:
            final.append(cl)
            
        cl += 1
    return final

#matriz = [[-3,-1],[0,3],[-1,-2]]
#print(linha_neg(matriz))

def coluna_neg(matriz):
    coluna = len(matriz[0])
    cc = 0
    linha = len(matriz)
    final = []
    while cc < coluna:
        cl = 0
        neg_lin = 0
        while cl < linha:
            if matriz[cl][cc] < 0:
                neg_lin += 1
            cl += 1
            
        if neg_lin == cl:
            final.append(cc)
            
        cc += 1
    return final
        
#matriz = [[-3,-1,0,-4],[-1,-1,-1,-5],[-1,0,4,-1]]
#print(coluna_neg(matriz))

def exercicio_10(matriz):
    resposta = []
    resposta.append(linha_neg(matriz))
    resposta.append(coluna_neg(matriz))
    return resposta
    
#matriz = [[-3,-1,0,-4],[-1,-1,-1,-5],[-1,0,4,-1]]
#print(exercicio_10(matriz))

def exercicio_11(matriz):
    linha = len(matriz)
    cl = 0
    while cl < linha:
        coluna = len(matriz[cl])
        cc = 0
        while cc < coluna:
            if matriz[cl][cc] != matriz[cc][cl]:
                return print('Não é simétrica.')
            cc += 1   
        cl += 1 
    return print('É simétrica.')

'''linda = [[1,2,3],
        [2,4,3],
        [3,3,1]]'''
#exercicio_11(linda)
def linha_do_menor(matriz):
    linha = len(matriz)
    cl = 0
    menor = matriz[0][0]
    posicao = 0
    while cl < linha:
        coluna = len(matriz[cl])
        cc = 0
        while cc < coluna:
            if menor > matriz[cl][cc]:
                menor = matriz[cl][cc]
                posicao = cl
            cc += 1
        cl += 1
    return posicao

#bahia = [[5,2],[4,-1],[1,-3]]
#print(linha_do_menor(bahia))
def minmax(matriz, num):
    coluna = len(matriz[num])
    cc = 0
    maior = matriz[num][0]
    posicao = 0
    final = []
    while cc < coluna:
        if maior < matriz[num][cc]:
            maior = matriz[num][cc]
            posicao = cc
        cc += 1
    final.append(num)
    final.append(posicao)
    final.append(maior)
    return final
        
#matriz = [[1,2,3,4,5,6,7],[4,5,2,1,65,1],[0,1,2,3,4,2,1]]
#print(minmax(matriz,1))

def exercicio_12(matriz):
    num = linha_do_menor(matriz)
    final = minmax(matriz,num)
    return final

#matriz = [[1,2,3,4,5,6,7],[4,5,2,1,65,1],[0,1,2,3,2,1]]
#print(exercicio_12(matriz))

def exercicio_14(matriz):
    linha = len(matriz)
    final = []
    cont_l = 0
    while cont_l < linha:
        coluna = len(matriz[cont_l])
        cont_c = 0
        while cont_c < coluna:
            if not matriz[cont_l][cont_c] in final:
                final.append(matriz[cont_l][cont_c])
                
            cont_c += 1
            
        cont_l += 1
    return final

#linda = [[4,2,3],[2,1,0],[2,1,4,3,6]]
#print(exercicio_14(linda))

#Falta o exercicio 15

def menor_linha(matriz, linha):
    tam = len(matriz[linha])
    menor = matriz[linha][0]
    cont = 0
    coluna = 0
    while cont < tam:
        if menor > matriz[linha][cont]:
            menor = matriz[linha][cont]
            coluna = cont
        cont += 1
    final = [menor, coluna, linha]
    return final

def maior_coluna(matriz,lista):
    tam = len(matriz)
    maior = lista[0]
    coluna = lista[1]
    cont = 0
    rep = 0
    while cont < tam:
        if maior < matriz[cont][coluna]:
            rep += 1
        cont += 1
    if rep == 0:
        return True
    else:
        return False

def exercicio_13(matriz):
    tam = len(matriz)
    cont = 0
    rep = 0
    while cont < tam:
        dados = menor_linha(matriz, cont)
        if maior_coluna(matriz,dados):
            print(f'Possuí um ponto de cela! \nLinha: {dados[2]} \nColuna: {dados[1]}'
                  f'\nValor: {dados[0]}')
            rep += 1

        cont += 1
    if rep == 0:
        print('Não há ponto de cela.')

#matriz = [[6,-1,3], [6,8,5], [-1,-2,3]]
#exercicio_13(matriz)

def identificar_igual(matriz, linha, coluna):
    numero = matriz[linha][coluna]
    rep = 0
    linha = len(matriz)
    cont_l = 0
    while cont_l < linha:
        coluna = len(matriz[cont_l])
        cont_c = 0
        while cont_c < coluna:
            if matriz[cont_l][cont_c] == numero:
                rep += 1
            cont_c += 1
        cont_l += 1
    if rep > 1:
        return [numero, rep]

    return [numero, 0]

def checar_repeticao(final, numero):
    #Checar se já foi adicionado o número e seu número de repetições.
    if numero[1] > 0:
        tam = len(final)
        if tam == 0:
            final.append(numero)
            return final
        else:
            rep = 0
            cont = 0
            while cont < tam:
                if final[cont][0] == numero[0]:
                    rep += 1
                cont += 1
            if rep > 0:
                return final
            else:
                final.append(numero)
                return final
    else:
        return final



def exercicio_15(matriz):
    final = []
    linha = len(matriz)
    cont_l = 0
    while cont_l < linha:
        coluna = len(matriz[cont_l])
        cont_c = 0
        while cont_c < coluna:
            numero = identificar_igual(matriz=matriz, linha=cont_l, coluna=cont_c)
            final = checar_repeticao(final=final, numero=numero)
            cont_c += 1
        cont_l += 1

    tam = len(final)
    num = 0
    while num < tam:
        print(f'Número: {final[num][0]} & Repetições: {final[num][1]}')
        num += 1

matriz = [[6,-1,3], [6,-1,5], [-1,-2,3]]
exercicio_15(matriz=matriz)

#Todos os exercícios finalizados.