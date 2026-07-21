from interface import interface; from time import sleep; import json
from file import arquivo

arq = 'python/projects.py/sistema-cadastro/cadastros.json'

if not arquivo.arquivoexiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver pessoas cadrastadas', 'Cadrastas novas pessoas', 'Sair do sistema'])

    if resposta == 1:
        # opção de ler o arquivo txt
        arquivo.lerArquivo(arq)

    elif resposta == 2:
        interface.cabeca('Novo Cadrasto')
        nome = str(input('Nome: '))
        idade = interface.leiaint('idade: ')
        arquivo.cadastrar(arq, nome, idade)

    elif resposta == 3:
        interface.cabeca('Saindo do sistema.. Até logo!')
        sleep(0.5)
        print('...')
        print()
        exit()
        
    else:
        print('\033[31mERRO: Digite um número válido!\033[m')
    print()
    sleep(1.5)
