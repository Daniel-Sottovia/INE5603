def exercicio_01():
    num_01 = int(input('Insira um número: '))
    num_02 = int(input('Insira um número: '))
    cont = 1
    while num_01 <= num_02:
        if cont == 1:        
            print('Tabuada do {}'.format(num_01))
        print(num_01*cont)
        if cont == 10:
            num_01 += 1
            cont = 0
        cont += 1

def exercicio_02():
    quantidade = int(input('Digite a quantidade de números a informar: '))
    cont = 1
    soma = 0
    while cont <= quantidade:
        numero = int(input('Insira um número: '))
        inicial = 1
        fatorial = 1
        while inicial<=numero:
            fatorial = fatorial * inicial
            if inicial == numero:
                soma = soma + fatorial
            inicial += 1
            print(fatorial)
        cont += 1
    print(soma)
                     
def exercicio_03():
    linhas = int(input('Digite o número de linhas: '))
    cont = 1
    while cont <= linhas:
        colunas = 1
        while colunas <= cont:  
            print('*',end='')
            colunas += 1
        print('\n')
        cont+=1
        
def exercicio_04():
    linhas = int(input('Digite o número de linhas: '))
    total = linhas * 2
    cont = 1
    outro = 1
    while cont <= total:
        colunas = 1
        while colunas <= outro:
            print('*', end='')
            colunas += 1
        print('\n')
        cont += 1
        if cont <= linhas:
            outro += 1
        else:
            outro -= 1

def sequencia_infinita():
    numero = int(input('Digite um número: '))
    soma = 0
    cont = 0
    while cont < numero:
        inicial = 1
        fatorial = 1
        while inicial <= cont:
            fatorial = fatorial * inicial
            inicial += 1
        soma = soma + (1/fatorial)
        cont += 1
    print(soma)

def quantidades():
    numero = int(input('Digite um número: '))
    cont_par = 0
    cont_impar = 0
    maior = 0
    while numero >= 0:
        if numero % 2 == 0:
            cont_par += 1
        else:
            cont_impar += 1
            if numero > maior:
                maior = numero
        numero = int(input('Digite um número: '))
    print(f'{cont_par}, ', end='')
    print(f'{cont_impar}, ', end='')
    if maior != 0:
        print(f'{maior}')
    else:
        print('nenhum')

def graos():
    variavel = 1
    soma = 1
    contador = 1
    while contador < 64:
        variavel = soma + 1
        soma = soma + variavel
        contador += 1
    print(soma)

def serie():
    numero = int(input('Quantida de termos da série: '))
    termo_01 = 2
    termo_02 = 7
    termo_03 = 3
    cont = 1
    n = 0
    while cont <= numero:
        if cont % 3 == 1:
            print(f'{termo_01 * (2**n)}', end='')
        elif cont % 3 == 2:
            print(f'{termo_02 * (3**n)}', end='')
        else:
            print(f'{termo_03 * (4**n)}', end='')
        if cont % 3 == 0:
            n += 1
        cont += 1
        if cont <= numero:
            print(', ', end='')

def floyd():
    linhas = int(input('Digite o número de linhas: '))
    cont = 1
    numero = 1
    while cont <= linhas:
        colunas = 1
        while colunas <= cont:
            print(f'{numero}',end=' ')
            colunas += 1
            numero += 1
        print('', end='\n')
        cont+=1
