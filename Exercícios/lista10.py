import random
def exercicio_01():
    numeros = []
    quant = int(input('Digite um número: '))
    cont = 0
    while cont < quant:
        numeros.append(random.random())
        cont += 1
    return print(numeros)

def inputListaInteiros():
    return [int(ent) for ent in input().split()]

def exercicio_02():
    linda = inputListaInteiros()
    n = len(linda)
    cont = 0
    while cont < n:
        if linda[cont] < 0:
            linda[cont] = linda[cont] * (-1)
        cont += 1
    return print(linda)

def exercicio_03(bahia):
    maior = max(bahia)
    n = len(bahia)
    cont = 0
    while cont < n:
        bahia[cont] = bahia[cont] / maior
        cont += 1
    return print(bahia)

#sonho = [4,4,5,2,1,-3,6]
#exercicio_03(sonho)

def primo(num):
    cont = 0
    n = 1
    while n <= num:
        if num % n == 0:
            cont += 1
        n += 1
    if cont == 2:
        return True
    else:
        return False

def exercicio_04(vida):
    n = len(vida)
    primos = []
    cont = 0
    while cont < n:
        if primo(vida[cont]):
            primos.append(vida[cont])
        cont += 1
    return print(primos)

#vida = [5, 10, 4, 6, 81, 16, 21, 17]
#exercicio_04(vida)

def prox_primo(num):
    while True:
        if primo(num):
            return num
        num += 1

def final():
    num = int(input())
    prox_primo(num + 1)

def exercicio_05(quant, inicio):
    saudades = []
    cont = 0
    while cont < quant:
        saudades.append(prox_primo(inicio + 1))
        inicio = prox_primo(inicio + 1)
        cont += 1
    return print(saudades)

#exercicio_05(5, 80)

def exercicio_06(lista1, lista2):
    n1 = len(lista1)
    n2 = len(lista2)
    final = []
    cont = 0
    if n1 >= n2:
        while cont < n2:
            final.append(lista1[cont] * lista2[cont])
            cont += 1
        while cont < n1:
            final.append(lista1[cont])
            cont += 1
    elif n2 >= n1:
        while cont < n1:
            final.append(lista1[cont] * lista2[cont])
            cont += 1
        while cont < n2:
            final.append(lista2[cont])
            cont += 1
    else:
        while cont < n1:
            final.append(lista1[cont] * lista2[cont])
            cont += 1
    return print(final)

#lista1 = [2, 1, 5, 3, -1, 4]
#lista2 = [3, 2, 4, 2, 1, 9, 10, 11]
#exercicio_06(lista1,lista2)



