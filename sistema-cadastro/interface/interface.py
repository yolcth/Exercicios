def leiaint(msg):
    while True:
        try :
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mErro: O valor digitado está errado\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mErro: O usuário preferiu não continuar.\033[m')
            return 0
        else:
            return n

def linha(tam=40):
    return '-' * tam


def cabeca(texto):
    print(linha())
    print(texto.center(40))
    print(linha())
    

def menu(lista):
    cabeca('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[36m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc