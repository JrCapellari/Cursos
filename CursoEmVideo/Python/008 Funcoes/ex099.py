from time import sleep


def maior(* num):
    n = 0
    print('-' * 30)
    print('Valores: ', end='')
    for n in num:
        sleep(0.4)
        print(f'{n}', end=' ')
    print(f'\nForam {len(num)} valores')
    if n >= n:
        n = n
        print(f'O maior valor foi {n}')


# PROGRAMA PRINCIPAL
maior(1, 2, 8, 3, 7, 9)
maior(6)
maior(0)
maior()
