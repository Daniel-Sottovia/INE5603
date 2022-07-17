print('Acta non verba')

def informado():
    usur = int(input('Digite um número: '))
    num = 1
    if usur > 1:
        while num <= usur:
            resto = num % 2
            if resto != 0:
                print(num)
            num += 1

def decrescente():
    num = 20
    while num >= 0:
        print(num)
        num -= 1

def tabuada():    
    usur = int(input('Informe um número: '))
    num = 1
    while num <= 10:
        tabuada = usur * num
        print(tabuada)
        num += 1

def multiplos_crescente():
    usur = int(input('Informe um número: '))
    num = 1
    while num <= usur:
        resto = usur % num
        if resto == 0:
            print(num)
        num += 1
        
def produtorio():
    usur = int(input('Informe um número: '))
    num = 1
    produto = 1
    while num <= usur:
        produto = produto * num
        num += 1
    if produto % 2 == 0:
        print(f'{produto} é par.')
    else:
        print(f'{produto} é ímpar.')
        
def receba():
    soma = 0
    cont = 0
    while True:
        num = int(input('Digite: '))
        if num == 0:
            break
        soma += num
        cont += 1
        media = soma / cont
    print(f'Quantidade de números: {cont} \nSomatório: {soma} \nMédia dos números: {media}')
    
def contador_divisiveis():           
    usur = int(input('Insira um valor entre 1 e 9: '))
    while usur < 1 or usur > 9:
        usur = int(input('Insira um valor entre 1 e 9: '))
    num = 1
    cont = 0
    while num <= 1000:
        resto = num % usur
        if resto == 0:
            cont += 1
        num += 1
    print(f'Há {cont} divisíveis por {usur} no intervalo de 1 a 1000')


usur = int(input('Insira um número: '))
while usur <= 0:
    usur = int(input('Insira um número: '))
resto = usur % 9
quociente = usur // 9
cont = 2
resultado = 'A'
vibra = 1
cont_A = 1
cont_B = 0
cont_C = 0
while vibra <= quociente:
    while cont <= 9:
        if cont <= 3:
            resultado = resultado + 'A'
            cont_A += 1
        elif cont > 3 and cont <= 6:
            resultado = resultado + 'B'
            cont_B += 1
        elif cont > 6 and cont <= 9:
            resultado = resultado + 'C'
            cont_C += 1
        cont += 1
    vibra += 1
    cont = 1
cont = 1
while cont <= resto:
    if cont <= 3:
        resultado = resultado + 'A'
        cont_A += 1
    elif cont > 3 and cont <= 6:
        resultado = resultado + 'B'
        cont_B += 1
    elif cont > 6 and cont <= 9:
        resultado = resultado + 'C'
        cont_C += 1
    cont += 1

print(resultado)
print(f'A:{cont_A} B:{cont_B} C:{cont_C}')
    
    
    
    
    