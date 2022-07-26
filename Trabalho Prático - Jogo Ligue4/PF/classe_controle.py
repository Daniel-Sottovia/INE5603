from classe_jogador import Jogador
from classe_tabuleiro import Tabuleiro

class Controle():
    '''
    Vai controlar o jogo, iniciar o tabuleiro, chamar as jogadas e checar o vencedor.
    '''
    def __init__(self):
        self.matriz = Tabuleiro()
        self.iniciarJogo()

    def iniciarJogo(self):
        modelo = self.modeloJogo()
        self.matriz.mostrarMatriz()
        cont = 0
        modo = 'A'
        while True:
            print(f'Jogador {modo}')
            if not modelo:
                posicao = Jogador()
            elif modelo and modo == 'A':
                posicao = Jogador()
            elif modelo and modo == 'B':
                posicao = Jogador(auto=False)
                while not self.matriz.matrizAceita(jogada=posicao.getJogada()):
                    posicao = Jogador(auto=False)
                if self.matriz.matrizAceita(jogada=posicao.getJogada()):
                    print(posicao)
            while not self.matriz.matrizAceita(jogada=posicao.getJogada()):
                posicao = Jogador()
            linha = self.matriz.matrizOndeAdicionar(jogada=posicao.getJogada())
            self.matriz.matrizAdicionar(jogada=posicao.getJogada(), modelo=modo)
            self.matriz.mostrarMatriz()
            if self.checarLinhas(modo=modo, linha=linha) or self.checarColunas(modo=modo,jogada=posicao.getJogada()) or self.checarDiagonal(modo=modo, jogada=posicao.getJogada(), linha=linha):
                print(f'Vencedor jogador: {modo}')
                break

            cont += 1
            if cont % 2 == 0:
                modo = 'A'
            else:
                modo = 'B'
            if not self.jogadasDisponiveis():
                print('Empate!!! Não há mais jogadas disponíveis.')
                break


    def modeloJogo(self):
        modelo = int(input('Selecione: \n1) Humano x Humano \n2) Humano x Máquina \nModo selecionado 1 ou 2: '))
        if modelo == 1:
            return False
        elif modelo == 2:
            return True

    def jogadasDisponiveis(self):
        linha = 0
        rep = 0
        while linha < 6:
            coluna = 0
            while coluna < 7:
                if self.matriz.getMatriz()[linha][coluna] == 0:
                    rep += 1
                coluna += 1
            linha += 1
        if rep > 0:
            return True
        return False

    def checarLinhas(self, modo, linha):
        '''No caso 'linha' representa a linha na qual foi adicionada a última jogada e 'modo' se é o jogador A ou B'''
        coluna = 0
        rep = 0
        while coluna < 7:
            if self.matriz.getMatriz()[linha][coluna] == modo:
                rep += 1
            else:
                rep = 0
            if rep == 4:
                return True
            coluna += 1
        return False

    def checarColunas(self, modo, jogada):
        '''o termo 'jogada' representa a coluna escolhida e 'modo' se é jogador A ou B'''
        linha = 0
        rep = 0
        while linha < 6:
            if self.matriz.getMatriz()[linha][jogada] == modo:
                rep += 1
            else:
                rep = 0
            if rep == 4:
                return True
            linha += 1
        return False

    def checarDiagonal(self, modo, jogada, linha):
        '''o termo 'jogada' representa a coluna escolhida e 'modo' se é jogador A ou B'''
        cont_e = abs(linha - jogada)
        rep = 0
        cont_l = 0
        while cont_l < 6 and cont_e < 7:
            if self.matriz.getMatriz()[cont_l][cont_e] == modo:
                rep += 1
            else:
                rep = 0

            cont_l += 1
            cont_e += 1
            if rep == 4:
                return True
        if (linha + jogada) >= 7:
            cont_d = 6
            cont_l = (linha + jogada) - cont_d
        else:
            cont_d = linha + jogada
            cont_l = 0
        rep = 0
        while cont_l < 6 and cont_d >= 0:
            if self.matriz.getMatriz()[cont_l][cont_d] == modo:
                rep += 1
            else:
                rep = 0

            cont_l += 1
            cont_d = cont_d - 1
            if rep == 4:
                return True
        return False

controle = Controle()
