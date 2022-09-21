import pygame
import sys

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


def draw_board(board):
    for c in range(7):
        for r in range(6):
            pygame.draw.rect(screen, azul, (c * squaresize, r * squaresize + squaresize, squaresize, squaresize))
            pygame.draw.circle(screen, fundo, (
            int(c * squaresize + squaresize / 2), int(r * squaresize + squaresize + squaresize / 2)), raio)

    for c in range(7):
        for r in range(6):
            if board[r][c] == 'A':
                pygame.draw.circle(screen, vermelho, (int(c * squaresize + squaresize / 2), int(r * squaresize + squaresize / 2)), raio)
            elif board[r][c] == 'B':
                pygame.draw.circle(screen, amarelo, (int(c * squaresize + squaresize / 2), int(r * squaresize + squaresize / 2)), raio)
    pygame.display.update()

matriz = iniciar()

squaresize = 100
comprimento = 7 * squaresize
altura = 7 * squaresize
dimensao = (comprimento, altura)

vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
preto = (0, 0, 0)
azul = (0, 0, 255)
fundo = (255, 255, 255)

raio = int(squaresize/2 - 10)

pygame.init()

screen = pygame.display.set_mode(dimensao)
myfont = pygame.font.SysFont("monospace", 75)

jogador = 'A'
cont = 0
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, fundo, (0, 0, comprimento, squaresize))
            posx = event.pos[0]
            if jogador == 'A':
                pygame.draw.circle(screen, vermelho, (posx, int(squaresize/2)),raio )
            elif jogador == 'B':
                pygame.draw.circle(screen, amarelo, (posx, int(squaresize / 2)), raio)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, fundo, (0, 0, comprimento, squaresize))
            posx = event.pos[0]
            col = int(posx // squaresize)
            if matriz_aceita(matriz, col):
                resul = adicionar(matriz, posicao=col, jogador=jogador)
                matriz = resul[0]
                coordenadas = resul[1]
            print(f'Jogador {jogador}: {col}')

            imprimir(matriz)
            print()
            draw_board(matriz)

            if checar_linhas(matriz=matriz, jogador=jogador, linha=coordenadas[0]) or checar_colunas(matriz=matriz, jogador=jogador,coluna=coordenadas[1]) or checar_diagonal(matriz=matriz, jogador=jogador, linha=coordenadas[0], coluna=coordenadas[1]):
                print(f'Jogador {jogador} venceu !!!')
                game_over = True




            cont += 1
            if cont % 2 == 0:
                jogador = 'A'
            else:
                jogador = 'B'

            if game_over:
                pygame.time.wait(3000)


'''
Tem que rever o pq de não estar colocando na linha última linha, reassitir o vídeo do amigo, pois ele fez umas gambiarras 
'''
'''
Não está respeitando o matriz_aceita(), ou seja, ele não fica requisitando que se adicione uma coluna com vaga, ele pula para o próximo jogador
'''


