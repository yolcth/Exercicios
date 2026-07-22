import json; from utilidades import uteis
arquivo = 'python/projects/sistema_notas/json/notas.json'

lista = [
    '1 - Ver Alunos',
    '2 - Cadastrar Novo Aluno',
    '3 - Sair do Sistema'
]
uteis.interface('Sistema de notas')

while True:
    try:
        for value in lista:
            print(value)
        resposta = int(input('\nQual operação você deseja realizar no sistema? [1/3]: '))
        print()
        if resposta == 1:
            uteis.verAluno(arquivo)
        elif resposta == 2:
            nome = str(input('Nome do aluno: '))
            n1 = float(input('Nota 1: '))
            n2 = float(input('Nota 2: '))
            n3 = float(input('Nota 3: '))
            n4 = float(input('Nota 4: '))
            uteis.cadastrar(arquivo, nome, n1, n2, n3, n4)
        elif resposta == 3:
            print('Adeus.')
            break
        else:
            print('Número inválido. Tente novamente.\n')
    except (ValueError, NameError):
        print('\033[31mHouve um erro de digitação. Tente novamente.\033[m')
