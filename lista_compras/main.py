import uteis; from interface import inter; from time import sleep

arquivo = 'python/projects.py/lista_compras/historico.json'
inter.cabecalho('Sistema de Lista de Compras.')
print()

try:
    while True:
        lista = [
            '1 - Histórico de Compras;',
            '2 - Comprar e Registrar um novo produto;',
            '3 - Sair do Programa'
        ]
        for item in lista:
            print(item)
        ler = int(input('\nQual opção você deseja realizar? [1/3]: '))
        if ler == 1:
            print()
            uteis.ler(arquivo)
            print('-' * 35); print()
        elif ler == 2:
            inter.cabecalho('Cadastrando Produto')
            produto = str(input('Nome do produto: '))
            quantidade = int(input('Quantidade: '))
            uteis.cadastrar(arquivo, produto, quantidade); sleep(0.5); print('Cadastrando..'); sleep(0.5); print('..'); sleep(0.5)
            print(f'Produto cadastrado!')
            print('-' * 35); print()
        elif ler == 3:
            print('Muito obrigado! Volte sempre!')
            break
        else:
            print('\033[0;31mNúmero inválido. Tente novamente.\033[m')
except:
    print('\033[0;31mErro. Tente novamente.\033[m')
