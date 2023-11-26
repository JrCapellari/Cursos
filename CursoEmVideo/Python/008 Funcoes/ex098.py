from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} a {f} de {p} em {p}')
    if i < f:
        for c in range(i, f + 1, p):
            sleep(0.3)
            print(f'{c}', end=' ')
    if i > f:
        for c in range(i, f - 1, -p):
            sleep(0.3)
            print(f'{c}', end=' ')
    print()
    print(f'-' * 30)


# PROGRAMA PRINCIPAL
contador(0, 10, 1)
contador(10, 0, -2)
a = int(input('início: ').upper())
b = int(input('fim: ').upper())
d = int(input('passo: ').upper())
contador(a, b, d)

print('FIM')
