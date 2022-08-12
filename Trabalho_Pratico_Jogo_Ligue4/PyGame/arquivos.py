def geraMatriz():
    linha = 6
    coluna = 7
    matriz = []
    cont_l = 0
    while cont_l < linha:
        matriz.append([])
        cont_c = 0
        while cont_c < coluna:
            matriz[cont_l].append(' ')
            cont_c += 1
        cont_l += 1
    return matriz