def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par_impar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


# PROGRAMA PRINCIPAL
n = int(input('Digite valor para fatoração: '))
print(f'O fatorial de {n} é: {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2} e {f3}')

numero = int(input('Digite um numero: '))
if par_impar(numero):
    print(f'{numero} é PAR')
else:
    print(f'{numero} é IMPAR')
