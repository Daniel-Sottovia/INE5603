banco = [{'CPF': '18104319',
          'Nome': 'Daniel Sottovia Gomide',
          'idade':'22',
          'Curso':'Engenharia Mecânica',
          'Disciplinas':'EMC5204 EMC5335 EMC5419 EMC5443 INE5603'}]

def opcoes():
    escolha = int(input('1)Adicionar: \n2)Remover: \n3)Consultar estudantes: \n  Resposta: '))
    print(escolha)


def cadastro(banco):
    pos = len(banco) - 1
    nome = str(input('Nome: '))
    idade = str(input('Idade: '))
    curso = str(input('Curso: '))
    disciplina = str(input('Disciplinas: '))
    banco[pos]['Nome'] = nome
    banco[pos]['idade'] = idade
    banco[pos]['Curso'] = curso
    banco[pos]['Disciplinas'] = disciplina
    return banco
    
def entrada_cpf(banco):
    cpf = str(input('CPF: '))
    tam = len(banco)
    cont = 0
    rep = 0
    while cont < tam:
        if cpf == banco[cont]['CPF']:
            rep += 1
        cont += 1
    if rep == 0:
        banco.append({'CPF': cpf})
        cadastro(banco)
    return banco

print(entrada_cpf(banco))



