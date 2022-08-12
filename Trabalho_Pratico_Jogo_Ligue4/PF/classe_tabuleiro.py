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
        '''Retorna se na coluna escolhida na 'jogada' há lugar para adicionar'''
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
        '''Dentro da coluna escolhida, qual a linha será adicionada'''
        cont = 0
        final = 0
        while cont < 6:
            if self.matriz[cont][jogada] == 0:
                final = cont
            cont += 1
        return final

    def matrizAdicionar(self, jogada, modelo):
        '''Método para adicionar o elemento, 'jogada' representa a coluna escolhida e 'modelo' se é o jogador A ou B'''
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
