from interface import interface; import json

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # wt+ serve para criar o arquivo e escrever nele, caso ele não exista
        a.close() # aqui fechamos o arquivo para não ficar aberto, pois se ele ficar aberto, não podemos escrever nele
    except:
        print('Houve um erro.')
    else:
        print(f'Arquivo {nome} criado com sucesso')

    
def lerArquivo(nome):
    interface.cabeca('Pessoas Cadastradas')
    try:
        with open(nome, 'r') as a:
            dados = json.load(a)
            
        for pessoa in dados:
            print(f"{pessoa['nome']:<30}{pessoa['idade']:>3} anos.")
    except:
        print('Erro ao ler o arquivo.')


def cadastrar(arq, nome='desconhecido', idade=0):

    # try:      <-- Comente com #
    # Passo 1: Ler a lista de pessoas que já existem
    with open(arq, 'r') as a:
        lista_pessoas = json.load(a)
        
    # Passo 2: Criar o dicionário do novo usuário e colocar na lista
    nova_pessoa = {'nome': nome, 'idade': idade}
    lista_pessoas.append(nova_pessoa)
    
    # Passo 3: Salvar a lista atualizada de volta no arquivo
    with open(arq, 'w') as a:
        json.dump(lista_pessoas, a, indent=4)
            
    # except:   <-- Comente com #
    #     print(f'Houve um erro...')
    # else:     <-- Comente com #
    print(f'Novo registro de {nome} adicionado.')
