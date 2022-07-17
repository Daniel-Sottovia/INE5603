class Pessoa:
    def __init__(self, nome, endereco, telefone, email):
        self.nome = nome
        self.__endereco = endereco
        self.telefone = telefone
        self.email = email
        
    def __str__(self):
        return f'Pessoa {self.nome}'
    
    def __eq__(self, other):
        return self.nome == other.nome
        

class Estudante(Pessoa):
    def __init__(self, nome, endereco, telefone, email, graduacao):
        super().__init__(nome, endereco, telefone, email)
        self.graduacao = graduacao
        
    def __str__(self):
        return f'Estudante {self.nome}'
    
    def __eq__(self, other):
        if isinstance(other, Estudante):
            return self.graduacao == other.graduacao
        return False
        
class Data():
    def __init__(self, data):
        if self.checar_mes(data[3:5]):
            self.mes = str(data[3:5])
        else:
            self.mes = '01'
        if self.checar_dia(data):
            self.dia = str(data[0:2])
        else:
            self.dia = '01'
            
        self.ano = str(data[6:])
    
    def checar_mes(self, data):
        if int(str(data)) >= 1 and int(str(data)) <= 12:
            return True
        return False
    
    def checar_dia(self, data):
        if self.checar_mes(data[0:2]):
            month = [31,29,31,30,31,30,31,31,30,31,30,31]
            tam = int(str(data[3:5])) - 1
            if int(str(data[0:2])) > 0 and int(str(data[0:2])) <= month[tam]:
                return True
        return False
    
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
    
        

class Funcionario(Pessoa):
    def __init__(self, nome, end, tel, email, n_sala, salario, data):
        super().__init__(nome, end, tel, email)
        self._n_sala = n_sala
        self.__salario = salario
        self.data = Data(data)
        
    def __str__(self):
        return f'Funcionario {self.nome}'
        
class Professor(Funcionario):
    def __init__(self, nome, end, tel, email, n_sala, salario, data, horas, titulo):
        super().__init__(nome, end, tel, email, n_sala, salario, data)
        
        if self.carga_trabalho(horas):
            self.horas = horas
        else:
            self.horas = 40
        
        self.titulo = titulo
        
    def carga_trabalho(self, horas):
        if horas == 20 or horas == 40:
            return True
        return False
        
    def __str__(self):
        return f'Professor {self.nome}'

'''
daniel = Estudante(nome='Daniel', endereco = 'Rua Coronel', telefone = '67999294241', email = 'danielsottovia@gmail.com', graduacao = 'veterano')
print(daniel)
admissaoCaio = Data('11/03/2003')
print(admissaoCaio)
#Funcionou a classe Data.
caio = Funcionario(nome='Caio', end = 'Avenida Capital', tel = '489999', email = 'caiosottovia@gmail.com', n_sala = '01', salario = '1580.50', data='11/03/2003')
print(caio)
francesco = Professor(nome = 'Francesco', end = 'Ribeirão', tel = '679822', email = 'francescomaronese@gmail.com', n_sala = '04', salario = '21380.50', data='17/05/2023', horas=40, titulo='Médico')
print(francesco)


pedrinho = Pessoa(nome='Pedro', endereco = 'RJ', telefone = '2789900123', email = 'acordapedrinho@gmail.com')
pietro = Pessoa(nome='Pedro', endereco = 'SP', telefone = '5677743211', email = 'petrovingador@gmail.com')
print(pedrinho == pietro)

otavio = Estudante(nome='Otávio', endereco = 'Rua São Carlos', telefone = '67999895545', email = 'otaviopontes@gmail.com', graduacao = 'formando')
irmao_caio = Estudante(nome='Caio', endereco = 'Avenida da Capital', telefone = '67990291122', email = 'caiosottovia@gmail.com', graduacao = 'veterano')
print(daniel == pedrinho)
print(daniel == otavio)
print(caio == irmao_caio)
print(irmao_caio == caio)
'''
