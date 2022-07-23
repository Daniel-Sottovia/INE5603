import random

class Jogador():
    def __init__(self, auto=True):
        if auto:
            self.jogada = int(input('Jogada: '))
            while self.dominioJogada():
                self.jogada = int(input('Jogada: '))
        else:
            self.jogada = self.Robo()

    def dominioJogada(self):
        if self.jogada in [0,1,2,3,4,5,6]:
            return False
        return True

    def getJogada(self):
        return self.jogada

    def Robo(self):
        numero = random.randint(0,6)
        return numero

    def __str__(self):
        return f'Jogada: {self.jogada}'


class Tabuleiro():
    def __init__(self):
        self.matriz = self.geraMatriz()

    def geraMatriz(self):
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

    def matrizAceita(self, jogada):
        cont = 0
        rep = 0
        while cont < 6:
            if self.matriz[cont][jogada] == 0:
                rep += 1
            cont += 1
        if rep > 0:
            return True
        else:
            return False

    def matrizOndeAdicionar(self, jogada):
        cont = 0
        final = 0
        while cont < 6:
            if self.matriz[cont][jogada] == 0:
                final = cont
            cont += 1
        return final

    def matrizAdicionar(self, jogada, modelo):
        linha = self.matrizOndeAdicionar(jogada=jogada)
        if modelo == 'A':
            self.matriz[linha][jogada] = 'A'
        if modelo == 'B':
            self.matriz[linha][jogada] = 'B'

    def mostrarMatriz(self):
        cont = 0
        while cont < 6:
            coluna = 0
            while coluna < 7:
                print(self.matriz[cont][coluna], end=' ')
                coluna += 1
            print()
            cont += 1

    def getMatriz(self):
        return self.matriz


class Controle():
    '''
    Vai controlar o jogo, iniciar o tabuleiro, chamar as jogadas e checar o vencedor.
    '''
    def __init__(self):
        modelo = self.modeloJogo()
        self.matriz = Tabuleiro()
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
            if self.checarLinhas(modo=modo, linha=linha) or self.checarColunas(modo=modo, jogada=posicao.getJogada()) or self.checarDiagonal(modo=modo, jogada=posicao.getJogada(), linha=linha):
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
        '''o termo 'jogada' representa a coluna'''
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



teste = Controle()


'''jogo = Tabuleiro()
jogo.mostrarMatriz()
print(jogo.matrizAceita(jogada=3))
print(jogo.matrizOndeAdicionar(jogada=3))
jogo.matrizAdicionar(jogada=3, modelo='A')
jogo.mostrarMatriz()'''

