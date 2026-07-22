import json; from interface import inter

def cadastrar(arquivo, nome='Desconhecido', quantidade=0):
    try:
        with open(arquivo, 'r') as a:
            dados = json.load(a)
        novo_item = {'nome': nome, 'quantidade': quantidade}
        dados.append(novo_item)
        with open(arquivo, 'w') as a:
            json.dump(dados, a, indent=4)
    except (json.JSONDecodeError, FileNotFoundError):
        print('\033[31mErro ao abrir o arquivo.\033[m')
            

def ler(arquivo):
    try:
        inter.cabecalho('Histórico de Compras')
        with open(arquivo, 'r') as a:
            dados = json.load(a)
            for item in dados:
                print(f"Produto: {item['nome']} - Quantidade: {item['quantidade']}")
    except (json.JSONDecodeError, FileNotFoundError):
         print('\033[31mErro ao abrir o arquivo.\033[m')
        