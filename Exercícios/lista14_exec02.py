class CarroSimplicado():
    def __init__(self, capacidade:float, atual:float, consumo:float):
        self.capacidade = capacidade
        self.atual = atual
        self.consumo = consumo

    def abastece(self, volume:float):
        if volume <= (self.capacidade - self.atual):
            self.atual = self.atual + volume
            return True
        else:
            return False

    def get_gasolina(self):
        return self.atual

    def estaNaReserva(self):
        if self.atual <= 0.1 * self.capacidade:
            return True
        else:
            return False

    def consomeGasolina(self, distancia:float):
        litros = distancia / self.consumo
        if litros > self.atual:
            return 'Erro na distância informada.'
        elif litros <= self.atual:
            self.atual = self.atual - litros
            return self.atual

    def __str__(self):
        return f'Capacidade: {self.capacidade}l \nVolume de Gasolina: {self.atual:.2f}l \nEficiência: {self.consumo:.2f}km/l'

parati = CarroSimplicado(capacidade=70, atual=35.20, consumo=12.2)
print(parati)
print(parati.abastece(volume=12.34))
print(parati)
print(parati.consomeGasolina(200))
parati.consomeGasolina(300)
print(parati)
print(parati.estaNaReserva())
print(parati.consomeGasolina(100))
print(parati.abastece(60))
print(parati)
