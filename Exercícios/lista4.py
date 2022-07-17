def hipotenusa():
    cateto1 = float(input('Cateto 1: '))
    cateto2 = float(input('Cateto 2: '))
    if cateto1 > 0 and cateto2 > 0:
        hip = (cateto1 ** 2 + cateto2 ** 2)**(0.5)
        print(f'Hipotenusa: {hip}')
    else:
        print('Foi informado um valor negativo')
        
def maior_valor(): #Responde a questão 2 e 7;
    numero_1 = float(input('num1 -> '))
    numero_2 = float(input('num2 -> '))
    if numero_1 > numero_2:
        print(f'O maior valor é o {numero_1}')
    elif numero_1 == numero_2:
        print('Os números são igauis.')
    else:
        print(f'O maior valor é o {numero_2}')

def intervalo():
    numero = float(input('Inf um número: '))
    if numero > 0 and numero < 1:
        print('Está DENTRO do intervalo!')
    else:
        print('Está FORA do intervalo!')

def vogal():
    letra = input('Digite uma letra: ').lower()
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print(f'{letra} é uma vogal.')
    #if letra in ['a','e','i','o','u']:
        #print(f'{letra} é uma vogal.')
    else:
        print(f'{letra} é uma consoante.')
        
def multiplos():
    numero_1 = int(input('Inf o número 1: '))
    numero_2 = int(input('Inf o número 2: '))
    if numero_1 % numero_2 == 0:
        print(f'{numero_1} é multiplo de {numero_2}')

def descontos():
    valor_compra = float(input('Qual o valor da sua compra? '))
    if valor_compra >= 6999.00:
        valor_compra = valor_compra*0.85
        print(f'Você terá desconto de 15%, o novo valor a pagar será de R${valor_compra}')
    else:
        valor_compra = valor_compra*0.95
        print(f'Você terá desconto de 5%, o novo valor a pagar será de R${valor_compra}')

def caixa_eletronico():
    valor_saque = int(input('Digite o valor de saque: '))
    if valor_saque % 5 == 0:
        quociente_50 = valor_saque // 50
        resto_50 = valor_saque % 50
        quociente_10 = resto_50 // 10
        resto_10 = resto_50 % 10
        quociente_5 = resto_10 // 5
        print(f'Será entregue {quociente_50} notas de 50, {quociente_10} notas de 10 e {quociente_5} notas de 5.')
    else:
        print('Valor indisponível, dirija-se a outro caixa.')
     
def triangulo():
    a = float(input('Informe o lado A: '))
    b = float(input('Informe o lado B: '))
    c = float(input('Informe o lado C: '))
    if a > 0 and b > 0 and c > 0:
        if a-c < b < a+c and a-b < c < a+b and b-c < a < b+c:
            
    else:
        print('Você informou um valor negativo.')
        
    
def curso_de_piloto():
    altura = float(input('Inf a sua altura em metros: '))
    idade = int(input('Inf a sua idade: '))
    horas_voo = float(input('Inf as suas horas de voo: '))
    peso = float(input('Inf o seu peso: '))
    if altura >= 1.75 and 22 <= idade <= 40 and horas_voo > 1600 and 65 <= peso <= 95:
        print('Todas as condições foram atendidas para realizar o curso.')
    else:
        print('Nem todas as condições foram atendidas.')
    