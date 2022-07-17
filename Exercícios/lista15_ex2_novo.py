
class Automovel:
    def __init__(self, veiculo, marca, modelo, ano_fabri):
        self.veiculo = veiculo
        self.marca = marca
        self.modelo = modelo
        self.ano_fabri = ano_fabri
        
    def getNome(self):
        return self.veiculo

    def __str__(self):
        return f'({self.veiculo},{self.marca},{self.modelo},{self.ano_fabri}'

       
class Moto(Automovel):
    def __init__(self, veiculo, marca, modelo, ano_fabri, quilometragem):
        super().__init__(veiculo, marca, modelo, ano_fabri)
        self.quilometragem = quilometragem

    def __str__(self):
        return f'{self.veiculo},{self.marca},{self.modelo},{self.ano_fabri},{self.quilometragem}'
     
     
class Bike(Automovel):
    def __init__(self, veiculo, marca, modelo, ano_fabri):
        super().__init__(veiculo, marca, modelo, ano_fabri)
        
    def __str__(self):
        return f'{self.veiculo},{self.marca},{self.modelo},{self.ano_fabri}'


class Carro(Automovel):
    def __init__(self, veiculo, marca, modelo, ano_fabri, quilometragem):
        super().__init__(veiculo, marca, modelo, ano_fabri)
        self.quilometragem = quilometragem
        
    def __str__(self):
        return f'{self.veiculo}, {self.marca}, {self.modelo}, {self.ano_fabri}, {self.quilometragem}'

class Anuncio:
    def __init__(self, auto, valor_venda:float):
        self.auto = auto
        self.valor_venda = valor_venda

    def getValor(self):
        return self.valor_venda

    def setValor(self, novo_valor):
        self.valor_venda = novo_valor
        
    def __str__(self):
        return f'{self.auto},{self.valor_venda}'
        
class Revenda:
    def __init__(self):
        self.cad_anuncio = {}
        self.cad_venda = {}

    def NovoAnuncio(self, anuncio):
        self.cad_anuncio[anuncio.auto.getNome()] = anuncio
        
    def mostrarAnuncios(self):
        for veiculo in self.cad_anuncio.values():
            print(veiculo)

    def NovaVenda(self, venda):
        self.cad_venda[venda] = venda

    def getVendas(self):
        for venda in self.cad_venda:
            print(venda)

    def getMaiorVenda(self):
        maior = 0
        nome = ''
        for venda in self.cad_venda:
            if venda.getValor() > maior:
                maior = venda.getValor()
                nome = venda
        print(f'{nome}')

class Venda:
    def __init__(self, anuncio):
        self.anuncio = anuncio

    def setVenda(self, valor_final):
        self.anuncio.setValor(valor_final)
        return self.anuncio

    def getValor(self):
        return self.anuncio.getValor()

    def __str__(self):
        return f'{self.anuncio}'

c1 = Carro('Parati', 'VW', 'CLI 1.8', 1996, 60000)
a1 = Anuncio(c1, 25000.00)
revenda = Revenda()
revenda.NovoAnuncio(a1)
c2 = Bike('Caloi', 'Caloi', 'Aro 29', 2022)
a2 = Anuncio(c2, 700.00)
revenda.NovoAnuncio(a2)
c3 = Moto('Ninja','Kawasaki', '650', 2020, 30000)
a3 = Anuncio(c3, 23000.00)
revenda.NovoAnuncio(a3)
revenda.mostrarAnuncios()
print()
venda1 = Venda(a3)
venda1.setVenda(32000.00)
revenda.NovaVenda(venda1)
venda2 = Venda(a1)
venda2.setVenda(30000.00)
revenda.NovaVenda(venda2)
revenda.getVendas()
print()
revenda.getMaiorVenda()

