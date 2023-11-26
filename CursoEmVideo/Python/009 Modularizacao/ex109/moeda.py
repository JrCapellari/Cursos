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
    return f'{moeda}{p:.2f}'.replace('.', ',')
