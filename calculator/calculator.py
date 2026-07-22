import math
print('\n --- \033[4;30mCalculadora\033[m --- \n')

def exibir_escolha():
    contas = [
                '\033[4;37m1 - soma\033[m',
                '\033[4;35m2 - Subtração\033[m',
                '\033[4;36m3 - Divisão\033[m',
                '\033[4;37m4 - Multiplicacão\033[m',
                '\033[4;35m5 - potenciação\033[m',
                '\033[4;36m6 - raiz quadrada\033[m',
                '\033[4;37m7 - sair\033[m'
        ]
    for indice in contas:
        print(indice)

while True:
            exibir_escolha()
            try:
                conta = int(input('\nQual operação você deseja realizar? (1/7): '))
            except ValueError:
                print('Erro. Escolha apenas alguma das opções possíveis.')
                print()
                continue

            if conta == 7:
                print('\nAté a próxima! \n')
                break

            try:
                n1 = float(input('Digite o primeiro número: '))
                n2 = float(input('Digite o segundo número: '))
                print()
            except ValueError:
                print('Número inválido. Tente novamente.')
                continue

            if conta == 1:
                print(f'O resultado é de {n1 + n2:.2f}\n')

            elif conta == 2:
                print(f'O resultado é de {n1 - n2:.2f}\n')

            elif conta == 3:
                if n2 == 0:
                    print('Erro: Divisão por zero.\n')
                else:
                    print(f'O resultado é de {n1 / n2:.2f}\n')

            elif conta == 4:
                print(f'O resultado é de {n1 * n2:.2f}\n')

            elif conta == 5:
                 print(f'O resultado é de {n1 ** n2:.2e}\n')

            elif conta == 6:
                 if n1 < 0:
                    print('Erro: Raiz quadrada de número negativo não é permitida.\n')
                 else:
                     print(f'O resultado é de {math.sqrt(n1):.2f}\n')

            elif conta == 7:
                print('Até a próxima! \n')
                break

            else:
                print('Operação inválida.\n')
