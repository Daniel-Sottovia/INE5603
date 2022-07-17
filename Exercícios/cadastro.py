banco = {'04954199158':
             {'CPF':'04954199158',
              'Nome':'Daniel Sottovia Gomide',
              'Idade':22,
              'Curso':'Engenharia Mecânica'}}

def checagem(CPF,banco):
    cont = 0
    for individuos in banco:
        if CPF == individuos:
            cont += 1
    if cont == 0:
        return True
    else:
        return False

def cadastro(banco):
    CPF = str(input('CPF: '))
    while CPF != '-1':
        if checagem(CPF, banco):
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            while idade <= 0:
                idade = int(input('Idade: '))
            curso = str(input('Curso: '))
            banco[CPF] = {'CPF': CPF, 'Nome': nome,
                          'Idade': idade, 'Curso':curso}
        elif checagem(CPF, banco):
            print('CPF já existente!!!')
            print('Informe outro CPF ou -1 para parar o cadastro.')
            CPF = str(input('CPF: '))
        print('Para continuar o cadastramento insira um novo CPF ou digite -1.')
        CPF = str(input('CPF: '))
    return banco

def consulta(banco):
    dados = str(input('CPF à consultar: '))
    for cpf in banco:
        if cpf == dados:
            return print(banco[cpf])

def deletar(banco):
    dados = str(input('CPF à remover: '))
    cont = 0
    for cpf in banco:
        if cpf == dados:
            cont += 1
            del banco[cpf]
            print('Cadastro excluído!')
            print(banco)
            return banco
    if cont == 0:
        print('CPF não encontrado.')
    return banco

def interface(banco):
    while True:
        pergunta = str(input('Adicionar: 1 \nRemover: 2 \nConsultar: 3 \nDigite a sua escolha: '))
        if pergunta == '1':
            banco = cadastro(banco)
        elif pergunta == '2':
            banco = deletar(banco)
        elif pergunta == '3':
            consulta(banco)
        else:
            print('Obrigado pela atenção!!!')
            break

interface(banco)





interface(banco)



