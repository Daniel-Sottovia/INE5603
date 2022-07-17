
def exercio_em_aula():
    livro = []
    cont = 0
    while cont <= 5:
        num = int(input('Digite um número: '))
        livro.append(num)
        cont += 1
    cont = cont - 1
    while cont >= 0:
        print(f'{livro[cont]}', end=' ')
        cont = cont - 1


def maior_valor(livro):
    maior = livro[0]
    tam = len(livro) - 1
    cont = 0
    while cont <= tam:
        if livro[cont] > maior:
            maior = livro[cont]
        cont += 1
    return maior

def exercicio_01():
    livro = []
    while True:
        num = int(input('Digite um número: '))
        if num < 0:
            break
        livro.append(num)
    print(livro)
    print(maior_valor(livro))
    
def exercicio_03(linda):
    tam = len(linda) - 1
    while tam >= 0:
        print(f'{linda[tam]}', end = ' ')
        tam = tam - 1
 
#lista = ['S' , 'XVIII', 'Bahia', 15 , 4]
#exercicio_03(lista)

def exercicio_04(numeros):
    somatorio = 0
    tam = len(numeros) - 1
    while tam >= 0:
        if numeros[tam] % 2 == 0:
            somatorio += numeros[tam]
        tam = tam - 1
    return print(somatorio)

#numeros = [4, 6, 7, 8, 9, 10, 3, 5, 2]
#exercicio_04(numeros)

def exercicio_05(lista1, lista2):
    somatorio1 = sum(lista1)
    somatorio2 = sum(lista2)
    if somatorio1 > somatorio2:
        return True
    else:
        return False
    
#c1 = [3, 4, 5, 6, 7]
#c2 = [2, 9, 30]
#print(exercicio_05(c1, c2))
    
import math

def exercicio_06(gatinha):
    tam = len(gatinha) - 1
    cont = 0
    while cont <= tam:
        fatorial = math.factorial(gatinha[cont])
        print(f'{gatinha[cont]}! = {fatorial}')
        cont += 1
        
#linda = [ 4, 6, 2, 1, 7, 3]
#exercicio_06(linda)

from statistics import mean, median

def exercicio_07(notas):
    tam = len(notas) - 1
    cont = 0
    while cont <= tam:
        if notas[cont] < 0:
            return print('Notas informadas apresentam erros.')
        cont += 1
    resultado = [mean(notas), median(notas)]
    return resultado

#vida = [3, 5, 7.5]
#print(exercicio_07(vida))

def exercicio_08(respostas):
    gabarito = ['A', 'A', 'C', 'E', 'D', 'B', 'C', 'E', 'B', 'D']
    acertos = 0
    cont = 0
    while cont < 10:
        if gabarito[cont] == respostas[cont].upper():
            acertos += 1
        cont += 1
    return acertos

#daniel = ['c', 'a', 'e', 'b', 'd', 'c', 'd', 'b', 'a', 'd']
#erro = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
#print(exercicio_08(erro))

def exercicio_09(texto):
    tam = len(texto)
    inver = len(texto) -1 
    cont = 0
    aprov = []
    while cont < tam:
        if texto[cont] == texto[inver]:
            aprov.append(0)
        else:
            aprov.append(1)
        cont += 1
        inver = inver - 1
    if mean(aprov) == 0:
        return True
    else:
        return False

#palavra = 'danaad'
#print(exercicio_09(palavra))
    
def exercicio_10(frase):
    vogais = 0
    consoantes = 0
    zeros = 0
    diferentes = 0
    numeros = 0
    contador = 0
    tam = len(frase)
    aeiou = ['a', 'e', 'i', 'o', 'u']
    bdc = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z', 'w']
    while contador < tam:
        if frase[contador].lower() == 'a' or frase[contador].lower() == 'e' or frase[contador].lower() == 'i' or frase[contador].lower() == 'o' or frase[contador].lower() == 'u':
            vogais += 1
        else:
            diferentes += 1
        contador += 1
    numeros = diferentes - zeros
    resultado = [vogais, consoantes, diferentes, numeros]
    return resultado

#poema = 'doido buo'
#print(exercicio_10(poema))

def inputListaInteiros():
    return [int(ent) for ent in input().split()]


def final():
    linda = inputListaInteiros()
    n = len(linda)
    cont = 0
    maior_pri = linda[0]
    while cont < n:
        if linda[cont] > maior_pri:
            maior_pri = linda[cont]

        cont += 1
    return print(f'{maior_pri}')

final()

