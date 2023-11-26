def somar(a=0, b=0, c=0):  # parametros opcionais (add valor)
    """
    -> Faz a soma de três valores e exibe o resultado.
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return:  Sem retorno
    """
    soma = a + b + c
    print(f' Soma é {soma}')
    print('-' * 10)


# PROGRAMA PRINCIPAL
somar()
somar(3, 7, 10)
somar(5, 4)
somar(c=4, a=3)
help(somar)

