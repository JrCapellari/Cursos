from random import randint
from time import sleep


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print('Sorteando: ', end='')
    for n in lista:
        sleep(0.4)
        print(n, end='  ')


def soma_par():
    soma = 0
    pares = []
    for num in numeros:
        if num % 2 == 0:
            soma += num
            pares.append(num)
    print('\nOs pares são', end=' ')
    for n in pares:
        print(n, end=', ')
    print(f'\nE sua soma é: {soma}')


# PROGRAMA PRINCIPAL
numeros = list()
sorteia(numeros)
soma_par()
