class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
    def dizer_ola(self):
        print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
        f'anos e minha altura é {self.altura}m.')
        
    def cozinhar(self, receita):
        print(f'Estou cozinhando um(a): {receita}')
        
    def andar(self, distancia):
        print(f'Saí para andar. Volto quando completar {distancia} metros')
        

class ContaBancaria:
    def __init__(self, nome:str, saldo:float, senha:str):
        self.nome = nome
        self.__saldo = saldo
        self.__senha = senha
        
    def sacar(self, saque:float):
        if self.__saldo > saque and saque > 0:
            self.__saldo = self.__saldo - saque
            print(f'Saque de R${saque} realizado, saldo remanescente R${self.__saldo}')
        elif self.__saldo < saque:
            print('Saldo insuficiente.')
        elif saque < 0:
            print('Valor informado inválido.')
            
    def depositar(self, deposito:float):
        if deposito > 0:
            self.__saldo = self.__saldo + deposito
            print(f'Depósito de R${deposito}, saldo final R${self.__saldo}')
        elif deposito < 0:
            print('Valor informado inválido.')
            
    def set_senha(self, nova_senha:str):
        self.__senha = nova_senha
        print(f'Nova senha: {self.__senha}')
            
#daniel = ContaBancaria(nome='Daniel', saldo=1284.32, senha='SaudadesDaMorena')
#daniel.sacar(saque=43.20)
#daniel.depositar(deposito=100)
#daniel.set_senha(nova_senha='QueroTeVer')
        
class CarroSimplificado:
    def __init__(self, capacidade:int, atual:float, consumo_medio:float):
        self.capacidade = capacidade
        self.atual = atual
        self.consumo_medio = consumo_medio
        
    def abastece(self, volume:float):
        if (volume + self.atual) <= self.capacidade:
            self.atual = self.atual + volume
            return True
        else:
            return False
    
    def informaGasolina(self):
        print(f'{self.atual}')
        return self.atual
    
    def consomeGasolina(self, distancia:float):
        consumido = (distancia / self.consumo_medio)
        if consumido <= self.atual:
            self.atual = self.atual - consumido
        elif consumido > self.atual:
            print('Error ao informar a distância.')
    
    def estaNoReserva(self):
        if self.atual <= ( self.capacidade*0.1 ):
            return True
        else:
            return False
        
#porsche = CarroSimplificado(capacidade=85, atual=32.2, consumo_medio=12.1)
#porsche.consomeGasolina(distancia=300)
#porsche.informaGasolina()
#print(porsche.estaNoReserva())
#porsche.abastece(volume=50)
#porsche.informaGasolina()
#print(porsche.estaNoReserva())

class Pessoa:
    def __init__(self, nome='Daniel', rg='1684020', idade=22):
        self.nome = str(nome)
        self.__rg = str(rg)
        self.idade = int(idade)        
        
    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
        
    def setIdade(self, nova_idade:int):
        if nova_idade > 0:
            self.idade = nova_idade
            print(f'Idade: {self.idade}')
        else:
            print('Idade informada inválida!!!')
            
    def getRG(self):
        return self.__rg

#pedrinho = Pessoa(nome='Pedro', rg='13921726', idade=11)
#print(pedrinho.getNome())
#print(pedrinho.getIdade())
#print(pedrinho.getRG())
#pedrinho.setIdade(nova_idade=21)
#print(pedrinho.getIdade())
#print(pedrinho)

#gustavo = Pessoa()
#gustavo.getNome()
#gustavo.getIdade()
#gustavo.getRG()
    
class CadastroPessoas:
    def __init__(self):
        self.cad = []
    
    def adicionar_pessoa(self, NP):
        tam = len(self.cad)
        cont = 0
        rep = 0
        while cont < tam:
            if NP.getRG() == self.cad[cont].getRG():
                rep += 1
            cont += 1
        if rep == 0:
            self.cad.append(NP)
        else:
            print('Cadastro já existente')
        
    def consultar_individuo(self, rg):
        tam = len(self.cad)
        cont = 0
        while cont < tam:
            if rg == self.cad[cont].getRG():
                print(self.cad[cont].getNome())
                print(self.cad[cont].getIdade())
            cont += 1
            
    def listar_todos(self):
        tam = len(self.cad)
        cont = 0
        while cont < tam:
            print(self.cad[cont].getNome())
            cont += 1
            
    def maior_idade(self):
        tam = len(self.cad)
        cont = 0
        while cont < tam:
            if self.cad[cont].getIdade() >= 18:
                print(self.cad[cont].getNome())
            cont += 1
            
    def remover(self, ident):
        tam = len(self.cad)
        cont = 0
        while cont < tam:
            if ident == self.cad[cont].getRG() or ident == self.cad[cont].getNome():
               self.cad.pop(cont)
               return True
            cont += 1
        return False
            
#daniel = Pessoa('Daniel Sottovia', '1684020', 22)
#cadastro = CadastroPessoas()
#cadastro.adicionar_pessoa(NP = daniel)
#cadastro.consultar_individuo('1684020')
#cadastro.maior_idade()
#pedrinho = Pessoa(nome='Pedro', rg='13921726', idade=11)
#cadastro.adicionar_pessoa(NP = pedrinho)
#cadastro.listar_todos()
#cadastro.consultar_individuo('13921726')
#print(cadastro.consultar_individuo('13726'))
#print(cadastro.remover('1684020'))
#cadastro.adicionar_pessoa(NP = daniel)
#michel = Pessoa('Michel Duriex', '18104319', 23)
#cadastro.adicionar_pessoa(NP = michel)
#cadastro.listar_todos()
#cadastro.adicionar_pessoa(NP = daniel)

class Eleicao:
    def __init__(self):
        self.urna = []

    def votacao(self, voto=''):
        if voto.upper() in ['A','B','C','N','']:
            self.urna.append(voto)
        else:
            print('TENTE NOVAMENTE !!!')

    def getTotalVotos(self):
        tam = len(self.urna)
        print(f'Total de votos {tam}')
        cont_A = 0
        cont_B = 0
        cont_C = 0
        cont_N = 0
        rep = 0
        while rep < tam:
            if self.urna[rep] == 'A':
                cont_A += 1
            elif self.urna[rep] == 'B':
                cont_B += 1
            elif self.urna[rep] == 'C':
                cont_C += 1
            elif self.urna[rep] == 'N':
                cont_N += 1
            rep += 1
        brancos = tam - (cont_A + cont_B + cont_C + cont_N)
        perc_A = cont_A*100 / tam
        perc_B = cont_B*100 / tam
        perc_C = cont_C * 100 / tam
        print(f'Candidato A - {cont_A} votos, {perc_A:.2f}% percentual')
        print(f'Candidato B - {cont_B} votos, {perc_B:.2f}% percentual')
        print(f'Candidato C - {cont_C} votos, {perc_C:.2f}% percentual')
        print(f'Nulos       - {cont_N} votos, {cont_N*100 / tam:.2f}% percentual')
        print(f'Brancos     - {brancos} votos, {brancos*100 / tam:.2f}% percentual')

        if perc_A > perc_B and perc_A > perc_C:
            print('Candidato A foi ELEITO!!!')
        elif perc_B > perc_C and perc_B > perc_A:
            print('Candidato B foi ELEITO!!!')
        elif perc_C > perc_A and perc_C > perc_B:
            print('Candidato C foi ELEITO!!!')
        else:
            if perc_A == perc_B and perc_A != perc_C:
                print('Candidato A e B vão para o segundo turno.')
            elif perc_B == perc_C and perc_B != perc_A:
                print('Candidato B e C vão para o segundo turno.')
            elif perc_A == perc_C and perc_A != perc_B:
                print('Candidato A e C vão para o segundo turno.')
            else:
                print('Empate triplo entre os candidatos.')


regiao = Eleicao()
regiao.votacao(voto='A')
regiao.votacao(voto='B')
regiao.votacao(voto='A')
regiao.votacao(voto='A')
regiao.votacao(voto='C')
regiao.votacao(voto='N')
regiao.votacao()
regiao.votacao(voto='B')
regiao.votacao(voto='C')
regiao.votacao(voto='C')
regiao.votacao(voto='N')
regiao.votacao(voto='B')
regiao.votacao(voto='A')
regiao.votacao(voto='C')
regiao.votacao(voto='A')
regiao.votacao(voto='C')
regiao.votacao()
regiao.getTotalVotos()


