import random

class Jogador():
    def __init__(self, auto=True):
        '''Entrada 'auto' quando False usa o sistema de geração automática de jogada'''
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