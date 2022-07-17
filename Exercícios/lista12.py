def exercicio_01(matriz):
    tam = len(matriz)
    cont = 0
    soma = 0
    while cont < tam:
        soma = soma + matriz[cont][cont]
        cont += 1
    media = soma / cont
    return media

matriz = [[4,2,3],
          [4,5,6],
          [7,8,9]]

#print(exercicio_01(matriz))

def exercicio_02(matriz):
    tam = len(matriz)
    cont = 0
    num = matriz[cont][tam-1]
    while cont < tam:
        if matriz[cont][tam-1-cont] != num:
            return False
        cont += 1
    return True

matriz = [[1,2,3],
          [4,3,2],
          [3,2,1]]
#print(exercicio_02(matriz))
    
def soma_principal(matriz):
    tam = len(matriz)
    cont = 0
    soma = 0
    while cont < tam:
        soma = soma + matriz[cont][cont]
        cont += 1
    return soma

def soma_secundaria(matriz):
    tam = len(matriz)
    cont = 0
    soma = 0
    while cont < tam:
        soma = soma + matriz[cont][tam-1-cont]
        cont += 1
    return soma

def soma_cada_linha(matriz):
    tam = len(matriz)
    cl = 0
    lista = []
    while cl < tam:
        soma = 0
        cc = 0
        while cc < tam:
            soma = soma + matriz[cl][cc]
            cc += 1
        lista.append(soma)
        cl += 1
    return lista

def soma_cada_coluna(matriz):
    tam = len(matriz)
    cc = 0
    lista = []
    while cc < tam:
        soma = 0
        cl = 0
        while cl < tam:
            soma = soma + matriz[cl][cc]
            cl += 1
        lista.append(soma)
        cc += 1
    return lista

def exercicio_04(matriz):
    tam = len(matriz)
    princi = soma_principal(matriz)
    secund = soma_secundaria(matriz)
    if princi != secund:
        return False
    linhas = soma_cada_linha(matriz)
    colunas = soma_cada_coluna(matriz)
    cont = 0
    while cont < tam:
        if linhas[cont] != princi:
            return False
        if colunas[cont] != princi:
            return False
        cont += 1
    return True

matriz = [[1,2,3],[4,3,2],[3,2,1]]
linda = [[8,0,7],[4,5,6],[3,10,2]]

#print(exercicio_04(linda))

def diagonias_superior(matriz):
    tam = len(matriz)
    diag = 1
    while diag < tam:
        l = 0
        c = diag
        while c < tam:
            print(f'{matriz[l][c]}', end=' ')
            l += 1
            c += 1
        diag += 1
        print()
             

matriz = [[1,2,3,4],[4,5,6,7],[8,9,10,11],[11,12,13,14]]
#diagonias_superior(matriz)

def diagonal_canto_direito(matriz):
    tam = len(matriz)
    diag = 1
    while diag < tam:
        l = diag
        c = tam - 1
        while l < tam:
            print(f'{matriz[l][c]}', end=' ')
            l += 1
            c = c - 1
        diag += 1
        print()
        
#diagonal_canto_direito(matriz)
        
def diagonal_canto_esquerdo(matriz):
    tam = len(matriz)
    diag = 1
    cont = tam - 2
    while diag < tam:
        l = 0
        c = cont
        while l <= cont:
            print(f'{matriz[l][c]}', end=' ')
            l += 1
            c = c - 1
        cont = cont - 1
        diag += 1
        print()
        
#diagonal_canto_esquerdo(matriz)
        
def diagonal_inferior(matriz):
    tam = len(matriz)
    diag = 1
    while diag < tam:
        l = diag
        c = 0
        while l < tam:
            print(f'{matriz[l][c]}', end=' ')
            c += 1
            l += 1
        
        diag += 1
        print()
    
#diagonal_inferior(matriz)
        
def exercicio_03(matriz):
    tam = len(matriz)
    linha = 0
    while linha < tam:
        mult = matriz[linha][linha]
        coluna = 0
        while coluna < tam:
            matriz[linha][coluna] = matriz[linha][coluna]*mult
            coluna += 1
        linha += 1
    print(matriz)
    
#linda = [[2,3,5],[3,4,6],[4,5,7]]
#exercicio_03(linda)

def diagonal_infer(matriz):
    tam = len(matriz)
    diag = 1
    final = []
    while diag < tam:
        l = diag
        c = 0
        temp = []
        while l < tam:
            temp.append(matriz[l][c])
            c += 1
            l += 1
            
        diag += 1
        
        if 0 in temp:
            final.append(temp)
            
    return final

def diagonal_super(matriz):
    tam = len(matriz)
    diag = 1
    final = []
    while diag < tam:
        l = 0
        c = diag
        temp = []
        while c < tam:
            temp.append(matriz[l][c])
            l += 1
            c += 1
            
        diag += 1
            
        if 0 in temp:
            final.append(temp)
            
    return final

             
def exercicio_05(matriz):
    super = diagonal_super(matriz)
    infer = diagonal_infer(matriz)
    tam_s = len(super)
    cont_s = 0
    while cont_s < tam_s:
        print(f'{super[cont_s]}')
        cont_s += 1
    tam_i = len(infer)
    cont_i = 0
    while cont_i < tam_i:
        print(f'{infer[cont_i]}')
        cont_i += 1
 
matriz = [[1,0,1], [0,1,8], [4,9,5]]
exercicio_05(matriz)