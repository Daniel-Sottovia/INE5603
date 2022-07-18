class ContaBancaria():
    def __init__(self, nome, saldo, senha):
        self.nome = nome
        self.saldo = saldo
        self.__senha = senha

    def setSenha(self, nova_senha):
        self.__senha = nova_senha
        return f'Nova senha: {self.__senha}'

    def __str__(self):
        return f'Nome: {self.nome} Saldo: {self.saldo:.2f}'

    def Deposito(self, deposito):
        if deposito > 0:
            self.saldo = self.saldo + deposito
            return f'Saldo: {self.saldo}'
        else:
            return f'Erro no valor informado.'

    def Sacar(self, valor):
        if valor > 0 and valor < self.saldo:
            self.saldo = self.saldo - valor
            return f'Saque de R${valor:.2f} \nSaldo Final: R${self.saldo:.2f}'
        elif valor > 0 and valor > self.saldo:
            return f'Saldo Insuficiente.'
        else:
            return f'Erro no valor informado.'

daniel = ContaBancaria(nome='Daniel', saldo=2048.43, senha='5172')
print(daniel.Deposito(deposito=30))
print(daniel)
daniel.Sacar(valor=1034.22)
print(daniel)
print(daniel.Sacar(valor=2000.00))
print(daniel.Deposito(deposito=-200))
print(daniel.setSenha(nova_senha='1504'))
daniel.Deposito(deposito=1435.22)
print(daniel)