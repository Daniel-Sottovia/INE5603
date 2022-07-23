def exercicio_01(num):
    linha = 0
    tam = num - 1
    while linha < num:
        cont_tam = 0
        coluna = 0
        while cont_tam < tam:
            print(' ', end='')
            cont_tam += 1
        tam = tam - 1
        while coluna < num:
            print('*', end='')
            coluna += 1
        linha += 1
        print()
        
"""exercicio_01(2)
exercicio_01(3)
exercicio_01(5)
exercicio_01(8)"""

def quadrada(matriz):
    linha = len(matriz)
    cont_l = 0
    while cont_l < linha:
        if len(matriz[cont_l]) != linha:
            return False
        cont_l += 1
    return True

def exercicio_02(matriz):
    if quadrada(matriz):
        tam = len(matriz)
        final = []
        cont = 0
        diag = 1
        while cont < tam - 2:
            linha = 0
            test = []
            rep = 0
            while (tam-1-diag) >= 0:
                if matriz[linha][tam-1-diag] in test:
                    rep += 1
                test.append(matriz[linha][tam-1-diag])
                linha += 1
                diag += 1
            if rep == 0 and linha > 1:
                final.append(cont + 1)
            cont += 1
            diag = cont + 1
            
        return final
                
    else:
        return []

#matriz = [[1,1,-4],[2,-1,-2],[3,-2,1]]
#matriz = [[8,-3,1],[4,-4,2]]
#matriz = [[1,1,4],[1,1,2],[3,1,1]]
#matriz = [[1,2,3,4],[-1,2,4,5],[1,2,5,7],[0,5,7,-1]]
#print(exercicio_02(matriz))
    
class Player:
    def __init__(self, pl_id=0, cr=0):
        self.__playerID = pl_id
        self.__creditos = cr
        
    def __str__(self):
        return f'player id: {self.__playerID}, créditos: {self.__creditos}'
    
    def getPlayerID(self):
        return self.__playerID
    

class PlayerCS(Player):
    def __init__(self, pl_id, cr, timeFavorito='contra-terrorista', armaFavorita='rifle'):
        super().__init__(pl_id, cr)
        self.timeFavorito = timeFavorito
        self.armaFavorita = armaFavorita
    
    def __str__(self):
        return f'{Player.__str__(self)} , time favorito: {self.timeFavorito}, arma favorita: {self.armaFavorita}'

class CadastroPlayers():
    def __init__(self):
        self.cadastro = {}
    
    def adicionarPlayer(self, jogador):
        cont = 0
        for nome in self.cadastro:
            if nome == jogador.getPlayerID():
                cont += 1
        if cont == 0:
            self.cadastro[jogador.getPlayerID()] = jogador
        else:
            return False
    
    def mostrarPlayers(self):
        for jogador in self.cadastro:
            print(self.cadastro[jogador])
        
daniel = PlayerCS(pl_id=18104319, cr=576, timeFavorito='anjos', armaFavorita='espada')
#print(daniel.getPlayerID())
#print(daniel)


caio = PlayerCS(pl_id=3422, cr=76)
#print(caio)
elder = PlayerCS(123, 87, 'terrorista', 'sniper')
#print(elder)

ronaldo = Player(9, 12)

banco = CadastroPlayers()
banco.adicionarPlayer(jogador=ronaldo)
banco.adicionarPlayer(daniel)
banco.adicionarPlayer(caio)
print(banco.adicionarPlayer(daniel))
banco.adicionarPlayer(elder)
banco.mostrarPlayers()

'''banco.adicionarPlayer(caio)
print(banco.adicionarPlayer(daniel))
banco.adicionarPlayer(elder)
'''
        
        