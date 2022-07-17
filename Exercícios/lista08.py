def exercicio_01(num):
    cont = 1
    fatorial = 1
    while cont <= num:
        fatorial = fatorial * cont
        cont += 1
    return fatorial

def exercicio_02(N, P):
    soma = exercicio_01(N)/(exercicio_01(P)*exercicio_01(N-P))
    return soma

#N = int(input('N: '))
#P = int(input('P: '))
#print(exercicio_02(N,P))

def exercicio_03(quant):
    if quant <= 0:
        return
    cont = 0
    euler = 0
    while cont < quant:
        euler = euler + (1/exercicio_01(cont))
        cont += 1
    return euler

#print(exercicio_03(9))

def exercicio_04(var, quant):
    if quant <= 0:
        return
    cont = 0
    cosseno = 0
    potencia = 0
    while cont < quant:
        if cont % 2 == 0:
            cosseno = cosseno + ((var**potencia)/(exercicio_01(potencia)))
        else:
            cosseno = cosseno - ((var ** potencia) / (exercicio_01(potencia)))
        potencia += 2
        cont += 1
    return cosseno

#print(exercicio_04(var=1, quant=4))

def exercicio_05(var, quant):
    if quant <= 0:
        return
    cont = 0
    seno = 0
    potencia = 1
    while cont < quant:
        if cont % 2 == 0:
            seno = seno + ((var ** potencia) / (exercicio_01(potencia)))
        else:
            seno = seno - ((var ** potencia) / (exercicio_01(potencia)))
        potencia += 2
        cont += 1
    return seno

#print(exercicio_05(var=1, quant=3))

def exercicio_06(inicio, final, numero):
    if numero >= inicio and numero <= final:
        return True
    else:
        return False

#print(exercicio_06(inicio=10, final=30, numero=11))

def exercicio_07(numero, *args):
    if len(args) == 2 :
        print('Intervalo fechado.')
        if args[0] < args[1]:
            inicio = args[0]
            final = args[1]
            if numero >= inicio and numero <= final:
                return True
            else:
                return False
        else:
            inicio = args[1]
            final = args[0]
            if numero >= inicio and numero <= final:
                return True
            else:
                return False
    else:
        print('Intervalo aberto.')
        return False

#print(exercicio_07(50, 90, 80))

def exercicio_08(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False

#print(exercicio_08(5))

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

def prox_primo(num):
    while True:
        if primo(num):
            print(num)
            break
        num += 1

def final():
    num = int(input())
    prox_primo(num + 1)


final()