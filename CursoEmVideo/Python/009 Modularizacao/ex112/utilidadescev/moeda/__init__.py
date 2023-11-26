def aumentar(p=0, t=0, formato=False):
    r = p + (p*t/100)
    return r if formato is False else forma(r)


def diminuir(p=0, t=0, formato=False):
    r = p - (p*t/100)
    return r if formato is False else forma(r)


def dobro(p=0, formato=False):
    r = p * 2
    return r if formato is False else forma(r)


def metade(p=0, formato=False):
    r = p / 2
    return r if formato is False else forma(r)


def forma(p=0, moeda='R$'):
    return f'\t{moeda}{p:.2f}'.replace('.', ',')


def resumo(p=0, a=0, d=0):
    print('-' * 30)
    print('resumo do valor'.center(30).upper())
    print('-' * 30)
    print(f'Preço analisado: {forma(p)}')
    print(f'Dobro do preço: {dobro(p, True)}')
    print(f'Metade do preço: {metade(p, True)}')
    print(f'{a}% de aumento: {aumentar(p, a, True)}')
    print(f'{d}% de desconto: {diminuir(p, d, True)}')
    print(f'')
    print('-' * 30)
