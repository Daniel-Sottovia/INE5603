import math

def hipotenusa():
    cat1 = float(input('Informe o valor do cateto 1: '))
    cat2 = float(input('Informe o valor do cateto 2: '))
    hip = math.sqrt((cat1**2)+(cat2**2))
    return print(f'O valor da hipotenusa é {hip:.2f}')

def area_triangulo():
    base = float(input('Informe o valor da base: '))
    altura = float(input('Informe o valor da altura: '))
    area = (base * altura) / 2
    return print(f'A área do triângulo é de {area:.2f}')

def area_trapezio():
    base_inferior = float(input('Informe o valor da base inferior: '))
    base_superior = float(input('Informe o valor da base superior: '))
    altura = float(input('Informe o valor da altura: '))
    area = ((base_superior + base_inferior) * altura) / 2
    return print(f'A área do trapézio é de {area:.2f}')

def calculo():
    a = float(input('Informe o valor da constate: '))
    x = float(input('Informe o valor da variável: '))
    funcao = x ** a
    derivada = (a*(x**(a-1)))
    return print(f'Valor da função é {funcao:.2f} e da derivada é {derivada:.2f}')

def conversor():
    medida = float(input('Informe um medida em metros: '))
    milimetros = medida * 1000
    return print(f'entrada -> {medida} ; saída -> {milimetros}mm')

def introducao():
    nome = input('Qual seu nome? ')
    ano_nascimento = int(input('Qual seu ano de nascimento? '))
    idade = 2022 - ano_nascimento
    return print(f'{nome}, você tem {idade} anos de idade.')

def n_segundos():
    dia = int(input('Dias: '))
    horas = int(input('Horas: '))
    minutos = int(input('Minutos: '))
    segundos = int(input('Segundos: '))
    total = (dia * 86400) + (horas * 3600) + (minutos * 60) + segundos
    return print(f'Entrada: dias: {dia}; horas: {horas}; minutos: {minutos}; segundos {segundos}\n'
                 f'Saída: Total em segundos: {total}s')

def aumento_de_salario():
    salario = float(input('Qual o valor do salário atual? R$ '))
    aumento_percentual = float(input('Qual o valor percentual de aumento? '))
    salario_final = salario * (1 + (aumento_percentual / 100))
    return print(f'O salário com aumento de {aumento_percentual}% é de R${salario_final}')

def desconto_no_produto():
    preco_produto = float(input('Qual o preço do produto? R$  '))
    desconto = float(input('Qual o percentual de desconto? '))
    preco_final = preco_produto * (1 - (desconto / 100) )
    return print(f'O produto com desconto de {desconto}% é de R${preco_final}')

def tempo_de_viagem():
    distancia = float(input("Qual a distância a percorrer em km ? "))
    velocidade_média = float(input('Qual a velocidade média de deslocamento em km/h ? '))
    horas_totais = distancia / velocidade_média
    return print(f'O tempo de viagem será de {horas_totais:.1f} horas.')

def converter_temperatura():
    celsius = float(input('Qual a temperatura em Celsius? '))
    fahrenheit = ((9 * celsius) / 5 ) + 32
    return print(f'Para a temperatura de {celsius}°C, temos {fahrenheit}°F.')

def aluguel_de_carro():
    dias = int(input('Por quantos dias o carro foi alugado? '))
    km_rodados = float(input('Por quantos km foram rodados? '))
    custo = (60 * dias) + (0.15 * km_rodados)
    return print(f'O aluguel do carro por {dias} dias e {km_rodados} km rodados terá valor de R${custo}.')

def reducao_vida():
    cigarros_dia = int(input('Quantos cigarros você fuma por dia? '))
    cigarros_ano = float(input('Há quantos anos você fuma? '))
    dias_perdidos = ((cigarros_ano * 365 * cigarros_dia) * 10) // 1440
    return print(f'Com essa vida de fumante já foram perdidos {dias_perdidos} dias de vida.')
