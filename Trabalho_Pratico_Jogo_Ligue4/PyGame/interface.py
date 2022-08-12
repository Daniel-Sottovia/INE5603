import pygame

from arquivos import geraMatriz



def draw_board(win, board):
    height = 600
    width = 600
    tamanho = 600/3

    for i in range(1,3):
        pygame.draw.line(win, (0,0,0), (0, i*tamanho),(width, i*tamanho), 3)
        pygame.draw.line(win, (0, 0, 0), (i * tamanho, 0), (i * tamanho, height), 3)


def redraw_window(win, board):
    win.fill((255, 255, 255))
    draw_board(win, board)

def main():
    win = pygame.display.set_mode((600,600))
    pygame.display.set_caption('Jogo Ligue4')

    board = geraMatriz()

    redraw_window(win, board)
    pygame.display.update()

    while True:
        pass

main()
