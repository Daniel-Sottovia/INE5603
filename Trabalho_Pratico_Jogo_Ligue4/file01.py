import random

def iniciar():
    linha = 6
    coluna = 7
    matriz = []
    cont_l = 0
    while cont_l < linha:
        matriz.append([])
        cont_c = 0
        while cont_c < coluna:
            matriz[cont_l].append(0)
            cont_c += 1
        cont_l += 1
    return matriz

def jogada():
    numero = int(input('Jogada: '))
    if numero not in [0,1,2,3,4,5,6]:
        while True:
            numero = int(input('Jogada: '))
            if numero in [0,1,2,3,4,5,6]:
                break
    return numero

def matriz_aceita(matriz, posicao):
    cont = 0
    rep = 0
    while cont < 6:
        if matriz[cont][posicao] == 0:
            rep += 1
        cont += 1
    if rep > 0:
        return True
    else:
        return False

def matriz_onde_adicionar(matriz, posicao):
    cont = 0
    final = 0
    while cont < 6:
        if matriz[cont][posicao] == 0:
            final = cont
        cont += 1
    return final

def adicionar(matriz, posicao, jogador):
    while not matriz_aceita(matriz,posicao):
        posicao = jogada()
    linha = matriz_onde_adicionar(matriz, posicao)
    if jogador == 'A':
        matriz[linha][posicao] = 'A'
    if jogador == 'B':
        matriz[linha][posicao] = 'B'
    return [matriz,[linha,posicao]]

def imprimir(matriz):
    cont = 0
    while cont < 6:
        coluna = 0
        while coluna < 7:
            print(matriz[cont][coluna], end=' ')
            coluna += 1
        print()
        cont += 1


def checar_linhas(matriz, jogador, linha):
    #Método checa da esquerda para a direita, vendo se terá um sequência de 4.
    coluna = 0
    rep = 0
    while coluna < 7:
        if matriz[linha][coluna] == jogador:
            rep += 1
        else:
            rep = 0
        if rep == 4:
            return True
        coluna += 1
    return False

def checar_colunas(matriz, jogador, coluna):
    #Método checa de baixo para cima, vendo se terá uma sequência de 4.
    linha = 0
    rep = 0
    while linha < 6:
        if matriz[linha][coluna] == jogador:
            rep += 1
        else:
            rep = 0
        if rep == 4:
            return True
        linha += 1
    return False

def checar_diagonal(matriz, jogador, linha, coluna):
    #São duas diagonais, diagonal vindo da esquerda(primeiro caso estudado) e diagonal vindo da direita(segundo caso estudado);
    cont_e = abs(linha - coluna)
    rep = 0
    cont_l = 0
    while cont_l < 6 and cont_e < 7:
        if matriz[cont_l][cont_e] == jogador:
            rep += 1
        else:
            rep = 0

        cont_l += 1
        cont_e += 1
        if rep == 4:
            return True

    if (linha + coluna) >= 7:
        cont_d = 6
        cont_l = (linha + coluna) - cont_d
    else:
        cont_d = linha + coluna
        cont_l = 0
    rep = 0
    while cont_l < 6 and cont_d >= 0:
        if matriz[cont_l][cont_d] == jogador:
            rep += 1
        else:
            rep = 0

        cont_l += 1
        cont_d = cont_d - 1
        if rep == 4:
            return True
    return False

def checar_jogadas_disponiveis(matriz):
    linha = 0
    rep = 0
    while linha < 6:
        coluna = 0
        while coluna < 7:
            if matriz[linha][coluna] == 0:
                rep += 1
            coluna += 1
        linha += 1
    if rep > 0:
        return True
    return False

def robo(matriz):
    #Fazer o robo escolher um número.
    numero = random.randint(0,6)
    while not matriz_aceita(matriz, numero):
        numero = random.randint(0,6)
    print(f'Jogada: {numero}')
    return numero

def modo_de_jogar():
    modo = int(input('Selecione: \n1) Humano x Humano \n2) Humano x Máquina \nModo selecionado 1 ou 2: '))
    if modo == 1:
        return False
    elif modo == 2:
        return True


def individuo_A_B():
    modo = modo_de_jogar()
    matriz = iniciar()
    imprimir(matriz)
    cont = 0
    jogador = 'A'
    while True:
        print(f'Jogador {jogador}')
        if not modo:
            posicao = jogada()
        elif modo and jogador == 'A':
            posicao = jogada()
        elif modo and jogador == 'B':
            posicao = robo(matriz)
        resul = adicionar(matriz=matriz, posicao=posicao, jogador=jogador)
        matriz = resul[0]
        coordenadas = resul[1]
        imprimir(matriz)
        if checar_linhas(matriz=matriz, jogador=jogador, linha=coordenadas[0]) or checar_colunas(matriz=matriz, jogador=jogador, coluna=coordenadas[1]) or checar_diagonal(matriz=matriz, jogador=jogador, linha=coordenadas[0], coluna=coordenadas[1]):
            return print(f'Vencedor jogador: {jogador}')
        cont += 1
        if cont % 2 == 0:
            jogador = 'A'
        else:
            jogador = 'B'
        if not checar_jogadas_disponiveis(matriz=matriz):
            return print('Empate!!! Não há mais jogadas disponíveis.')


individuo_A_B()


'''
matriz = [[0,0,0,0,0,1,0],
          [0,0,0,0,0,1,0],
          [0,0,1,0,0,1,1],
          [0,0,0,0,1,1,0],
          [0,1,0,1,1,1,0],
          [0,1,1,1,1,1,0]]

print(checar_diagonal(matriz=matriz, jogador=1, linha=2, coluna=6))
'''

"""
deus = adicionar(matriz=matriz, posicao=5, jogador='A')
        
imprimir(deus)
"""

"""
Sequência do pensamento: Jogador escolhe a posição, eu checo se tem espaço livre 
na coluna, depois checo qual a posição mais baixa livre na coluna, aí faço a substituição
do valor na coluna, agora alterno o jogador e repito o processo.
"""