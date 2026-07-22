from interface import uteis, inter; from time import sleep

arquivo = 'python/projects/lista_compras/historico.json'
inter.cabecalho('Sistema de Lista de Compras.')
print()

lista = [
    '1 - Histórico de Compras;',
    '2 - Comprar e Registrar um novo produto;',
    '3 - Sair do Programa'
]

while True:
    for item in lista:
        print(item)
    try:
        ler = int(input('\nQual opção você deseja realizar? [1/3]: '))
    except ValueError:
        print('\033[0;31mNúmero inválido. Tente novamente.\033[m')
        continue
    if ler == 1:
        print()
        uteis.ler(arquivo)
        print('-' * 35); print()
    elif ler == 2:
        inter.cabecalho('Cadastrando Produto')
        try:
            produto = str(input('Nome do produto: '))
            quantidade = int(input('Quantidade: '))
        except (NameError, ValueError):
            print('\033[0;31mNúmero inválido. Tente novamente.\033[m')
            continue
        uteis.cadastrar(arquivo, produto, quantidade)
        sleep(0.5); print('Cadastrando..'); sleep(0.5); print('..'); sleep(0.5)
        print(f'Produto cadastrado!')
        print('-' * 35); print()
    elif ler == 3:
        print('Muito obrigado! Volte sempre!')
        break
    else:
        print('\033[0;31mNúmero inválido. Tente novamente.\033[m')
