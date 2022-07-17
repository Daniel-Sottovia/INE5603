class Tela():
    def __init__(self, matriz_pixels):
        self._tela = matriz_pixels
        
    def getTelas(self):
        return self._tela
    
class TelaMobile(Tela):
    def __init__(self, matriz):
        if self.dimensaoLinha(matriz) and self.dimensaoColuna(matriz):
            super().__init__(matriz)
        else:
            super().__init__(self.CriarMatriz())
        
    def dimensaoLinha(self, matriz):
        tam = len(matriz)
        if tam >= 300 and tam <= 1024: #300 e 1024
            return True
        else:
            return False
        
    def dimensaoColuna(self, matriz):
        linha = len(matriz)
        cont = 0
        while cont < linha:
            coluna = len(matriz[cont])
            if coluna >= 300 and coluna <= 762: # 300 e 762
                pass
            else:
                return False
            cont += 1
            
        return True
    
    def CriarMatriz(self):
        matriz = []
        linha = 800 # 800
        coluna = 600 # 600
        cont_l = 0
        while cont_l < linha:
            matriz.append([])
            cont_c = 0
            while cont_c < coluna:
                matriz[cont_l].append(0)
                cont_c += 1
            cont_l += 1
            
        return matriz
    

def criador(linha, coluna):
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

"""eu = criador(4,7)
daniel = TelaMobile(eu)
print(daniel.getTelas())
voce = criador(4,8)
caio = TelaMobile(voce)
print(caio.getTelas())"""

class PossuiQuadrado(Tela):
