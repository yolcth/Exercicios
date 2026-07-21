import json
def interface(nome):
    l = 4 + len(nome)
    print('-' * l)
    print(f'  {nome}')
    print('-' * l)

def cadastrar(arquivo, nome, n1, n2, n3, n4):
    interface('Cadastro de Aluno')
    with open(arquivo, 'r') as arq:
        add = json.load(arq)
    
    lista_notas = [n1, n2, n3, n4]
    novo_aluno = {'nome': nome, 'notas': lista_notas}
    add.append(novo_aluno)

    with open(arquivo, 'w') as arq:
        json.dump(add, arq, indent=4)

def verAluno(arquivo):
    interface('Histórico de alunos')
    with open(arquivo, 'r') as a:
        pessoas = json.load(a)
        for pessoa in pessoas:
            print(f'Nome: {pessoa["nome"]}, Notas: {pessoa["notas"]}')
        interface('Lista Encerrada.')
        print()