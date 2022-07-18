class Pessoa():
    def __init__(self, nome='Daniel', rg='04954199158', idade=22):
        self.nome = nome
        self.__rg = rg
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def setIdade(self, nova_idade):
        if nova_idade > 0:
            self.idade = nova_idade

    def getRG(self):
        return self.__rg

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'


class CadastroPessoas():
    def __init__(self):
        self.cadastro = {}

    def adicionarPessoa(self, pessoa):
        if pessoa.getRG() not in self.cadastro:
            self.cadastro[pessoa.getRG()] = pessoa
        else:
            print('Cadastro já existente.')

    def consulta(self, dados):
        for cadastro in self.cadastro:
            if dados == cadastro:
                print(self.cadastro[cadastro])

    def remover(self, dado):
        for cadastro in self.cadastro:
            if dado == cadastro or dado == self.cadastro[cadastro].getNome():
                self.cadastro.pop(cadastro)
                return True
        else:
            return False

    def maiorIdade(self):
        maior = 0
        identificacao = ''
        for cadastro in self.cadastro:
            if self.cadastro[cadastro].getIdade() > maior:
                maior = self.cadastro[cadastro].getIdade()
                identificacao = self.cadastro[cadastro]
        print(identificacao.getNome())

    def listarTodos(self):
        for cadastro in self.cadastro:
            print(self.cadastro[cadastro])

caio = Pessoa(nome='Caio', rg='04544267601', idade=19)
daniel = Pessoa()
print(daniel)
veronika = Pessoa(nome='Veronika', idade=55, rg='18104319022')
guilherme = Pessoa(nome='Guilherme', idade=30, rg='17177789056')
banco = CadastroPessoas()
banco.adicionarPessoa(caio)
banco.adicionarPessoa(daniel)
banco.adicionarPessoa(veronika)
banco.adicionarPessoa(guilherme)
banco.adicionarPessoa(daniel)
banco.listarTodos()
banco.consulta(dados='04544267601')
print(banco.consulta(dados='1684020'))
banco.maiorIdade()
banco.listarTodos()
banco.remover(dado='Daniel')
banco.listarTodos()