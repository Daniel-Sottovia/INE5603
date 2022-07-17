def quadrada(matriz):
    linha = len(matriz)
    cont_l = 0
    while cont_l < linha:
        coluna = len(matriz[cont_l])
        if coluna != linha:
            return False
        cont_l += 1
    return True