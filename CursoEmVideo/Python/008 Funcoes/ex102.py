def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) mostra ou não o calculo
    :return: Retorna o valor fatorial de n
    """
    r = 1
    print(f'{n}! =', end=' ')
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        r *= c
    return r


# PROGRAMA PRINCIPAL
print(f'{fatorial(5, True)}')
# help(fatorial)
