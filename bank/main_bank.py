from uteis import util; from time import sleep
from uteis import cadastro; from uteis import interface
import json

arquivo = 'python/projects/bank/historico.json'

util.menu()

while True:
    lista = [
        '1 - Sou cadastrado, quero fazer o Login',
        '2 - Não sou cadastrado, quero me cadastrar',
        '3 - Quero sair do banco'
    ]
    for i in lista:
        print(i)
    situacao = int(input('\nQual operação você deseja realizar? [1/3]: '))
    if situacao == 2:
        nome = str(input('Digite o seu nome: '))
        idade = int(input('Digite a sua idade: '))
        if idade < 18:
            print('Você é menor de idade. Não pode se cadastrar.')
            break
        senha = str(input('Digite a sua senha: '))
        cadastro.cadastrar(arquivo, nome, idade, senha)
    elif situacao == 3:
        print('Até logo.')
        break
    if situacao == 1:
        interface.texto('Seu Login')
        usuario = str(input('Digite o seu nome: '))
        senha = str(input('Digite a sua senha: '))
        conta, logado = cadastro.login(arquivo, usuario, senha)
        if logado == True:
            print(f'Seja bem vindo(a) ao nosso sistema de banco, fizemos o melhor para que o usuário possa ter uma ótima experiência!')
            while True:
                print()
                util.options()
                sleep(0.5)
                escolha = int(input('\nO que você deseja fazer? (1/5): '))
                print()              
                if escolha == 5:
                    print('Muito obrigado por usar o nosso sistema bancário! Volte sempre!\n')
                    exit()

                elif escolha == 1:
                    util.ver_saldo(conta['saldo'])

                elif escolha == 2:

                    deposito = util.depositar_dinheiro(conta['saldo'])
                    conta['saldo'] += deposito
                    with open(arquivo, 'r') as a:
                        dados = json.load(a)
                    for usuario_dados in dados:
                        if usuario_dados['nome'] == conta['nome']:
                            usuario_dados['saldo'] = conta['saldo']
                    with open(arquivo, 'w') as a:
                        json.dump(dados, a, indent=4)

                elif escolha == 3:
                    retirar = util.retirar_dinheiro(conta['saldo'])
                    with open(arquivo, 'r') as a:
                        dados = json.load(a)
                    for usuario_dados in dados:
                        if usuario_dados['nome'] == conta['nome']:
                            usuario_dados['saldo'] -= retirar
                    with open(arquivo, 'w') as a:
                        json.dump(dados, a, indent=4)


                    sleep(0.5)   
                elif escolha == 4:
                    saldo_inicial = util.transferencia(saldo_inicial, nome)

        elif logado == False:
            print('Não encontramos a conta. Nome ou senha inválidos.\n')
            break
