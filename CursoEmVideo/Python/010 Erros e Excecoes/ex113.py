def leiaint(n):
    while True:
        try:
            num = int(input(n))
        except(ValueError, TypeError):
            print('ERRO: Digite apenas numeros inteiros')
            continue
        except(KeyboardInterrupt):
            print('\nPrograma parou')
            return 0
        else:
            return num


def leiafloat(n):
    while True:
        try:
            nf = float(input(n))
        except(ValueError, TypeError):
            print('ERRO: Digite um número real')
            continue
        except(KeyboardInterrupt):
            return 0
        else:
            return nf


# PROGRAMA PRINCIPAL
num = leiaint('Digite um número inteiro: ')
n = leiafloat('Digite um número real: ')
print(f'Número inteiro foi {num} e número real foi {n:.2f} ')
