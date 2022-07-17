def inputMatriz(qtLinhas):
    r = []
    for l in range(qtLinhas):
        r.append([int(ent) for ent in input().split()])
    return r

def par(num):
    if num % 2 == 0:
        return True
    return False

def abaixoPrincipal():
    num = int(input())
    matriz = inputMatriz(num)
    tam = len(matriz)
    cont = 1
    soma = 0
    while cont < tam:
        l = cont
        c = 0
        while l < tam:
            if par(matriz[l][c]):
                soma += 1
            l += 1
            c += 1
        cont += 1
    return print(soma)

abaixoPrincipal()
