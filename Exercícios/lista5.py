def tipos_triangulos():
    ang_1 = float(input('Digite um valor de ângulo: '))
    ang_2 = float(input('Digite um valor de ângulo: '))
    ang_3 = float(input('Digite um valor de ângulo: '))
    soma = ang_1 + ang_2 + ang_3
    if soma <= 180:
        if ang_1 < 90 and ang_2 < 90 and ang_3 < 90:
            print('Trata-se de um triângulo Acutângulo, pois todos os ângulos são menores que 90°.')
        elif ang_1 == 90 or ang_2 == 90 or ang_3 == 90:
            print('Trata-se de um triângulo Retângulo, pois possuí um ângulo com medida igual a 90°.')
        else:
            print('Trata-se de um triângulo Obtusângulo, pois possuí uma ângulo obtuso, maior que 90°.')
    else:
        print('A soma dos ângulos ultrapassou 180°.')

def maior_menor():
    n_1 = float(input('Digite um número: '))
    n_2 = float(input('Digite um número: '))
    n_3 = float(input('Digite um número: '))
    maior = []
    menor = []
    if n_1 > n_2 and n_1 > n_3:
        maior = n_1
        if n_2 < n_3:
            menor = n_2
        else:
            menor = n_3
    elif n_2 > n_1 and n_2 > n_3:
        maior = n_2
        if n_1 < n_3:
            menor = n_1
        else:
            menor = n_3
    else:
        maior = n_3
        if n_1 < n_2:
            menor = n_1
        else:
            menor = n_2
    print(f'O maior valor é {maior} e o menor valor é {menor}.')

def descontos():
    nivel_engajamento = input('Qual o seu nível de engajamento? ').lower()
    valor_compra = float(input('Qual o valor da compra? R$ '))
    if valor_compra > 100:
        if nivel_engajamento == 'seguidor':
            print(f'Haverá desconto de 5%, com preço final de R${valor_compra*0.95:.2f}')
        elif nivel_engajamento == 'comentarista':
            print(f'Haverá desconto de 8%, com preço final de R${valor_compra * 0.92:.2f}')
        elif nivel_engajamento == 'fã':
            print(f'Haverá desconto de 12%, com preço final de R${valor_compra * 0.88:.2f}')
        else:
            print('Não há descontos, nível de engajamento não atingido.')
    else:
        print('Não há descontos, valor da compra não atingido.')

def convertor_temperatura():
    unidade_medida = input('Qual a unidade de medida? ').lower()
    valor_temperatura = float(input('Qual o valor da temperatura? '))
    if unidade_medida == 'celsius':
        fahrenheit = (valor_temperatura * 1.8) + 32
        kevin = (valor_temperatura + 273)
        print(f'Fahrenheit = {fahrenheit:.2f}°F')
        print(f'Kelvin = {kevin:.2f}°K')
    elif unidade_medida == 'fahrenheit':
        celsius = (valor_temperatura - 32) / 1.8
        kevin = (celsius + 273)
        print(f'Celsius = {celsius:.2f}°C')
        print(f'Kelvin = {kevin:.2f}°K')
    elif unidade_medida == 'kelvin':
        fahrenheit = ((valor_temperatura - 273) * 1.8) + 32
        celsius = (valor_temperatura - 273)
        print(f'Fahrenheit = {fahrenheit:.2f}°F')
        print(f'Celsius = {celsius:.2f}°C')
    else:
        print('Erro ao informar unidade de medida.')

def modelos_triangulos():
    ang_1 = float(input('Digite um ângulo: '))
    ang_2 = float(input('Digite um ângulo: '))
    ang_3 = float(input('Digite um ângulo: '))
    soma = ang_1 + ang_2 + ang_3
    if ang_1 >= 0 and ang_2 >= 0 and ang_3 >= 0:
        if ang_1 > abs(ang_2- ang_3) and ang_1 < (ang_2 + ang_3) and ang_2 > abs(ang_1- ang_3) and ang_2 < (ang_1 + ang_3) and ang_3 > abs(ang_2- ang_1) and ang_1 < (ang_2 + ang_1):
            if ang_1 == ang_2 and ang_1 == ang_3:
               print('Trata-se de um triângulo equilátero.')
            elif ang_1 == ang_2 or ang_2 == ang_3 or ang_1 == ang_3:
                print('Trata-se de um triângulo isósceles.')
            else:
                print('Trata-se de um triângulo escaleno.')
        else:
            print('A condição de existência do triângulo não é respeitada.')
    else:
        print('Foi informado um valor negativo.')

def estado_fisico():
    pressao = float(input('Entrade de Pressão [kPa] : '))
    temperatura = float(input('Entrade de Temperatura [°C] : '))
    if pressao == 100:
        if temperatura < 0:
            print('Sólido.')
        elif temperatura == 0:
            print('Mistura sólido-líquido.')
        elif temperatura < 100:
            print('Líquido.')
        elif temperatura == 100:
            print('Mistura líquido-vapor.')
        else:
            print('Gasoso.')
    elif pressao == 200:
        if temperatura == 120:
            print('Mistura líquido-vapor.')
        elif temperatura > 120:
            print('Gasoso')
        else:
            print('Valor informado de Temperatura para a devida Pressão não está presente no banco de dados.')
    elif pressao == 300:
        if temperatura == 133.6:
            print('Mistura líquido-vapor.')
        elif temperatura > 133.6:
            print('Gasoso.')
        else:
            print('Valor informado de Temperatura para a devida Pressão não está presente no banco de dados.')
    elif pressao == 400:
        if temperatura == 143.6:
            print('Mistura líquido-vapor.')
        elif temperatura > 143.6:
            print('Gasoso.')
        else:
            print('Valor informado de Temperatura para a devida Pressão não está presente no banco de dados.')
    elif pressao == 500:
        if temperatura == 151.9:
            print('Mistura líquido-vapor.')
        elif temperatura > 151.9:
            print('Gasoso.')
        else:
            print('Valor informado de Temperatura para a devida Pressão não está presente no banco de dados.')
    else:
        print('Valor informado de Pressão informada não está presente no banco de dados.')
