def leiaint(n):
    while True:
        try:
            num = int(input(n))
        except(ValueError, TypeError):
            print('\33[31m:::ERRO::: Digite uma opção do MENU\33[m')
            continue
        except KeyboardInterrupt:
            print('\n:::ERRO::: PROGRAMA PAROU')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabeca(txt):
    print(linha())
    print(txt.center(42).upper())
    print(linha())


def menu(lista):
    cabeca('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\33[33m{c}\33[m - \33[34m{item}\33[m')
        c += 1
    print(linha())
    opc = leiaint('\33[33mSua opção:\33[m ')
    return opc
