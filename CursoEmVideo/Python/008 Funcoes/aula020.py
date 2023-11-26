def soma(a, b):
    s = a + b
    print(s)


def soma2(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'Soma de A + B = {s}')


def contador(*num):  # Desenpacota ((*) varios parametros)
    print(num)
    print(f'- Você passou {len(num)} parametros')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


# PROGRAMA PRINCIPAL
soma(2, 3)
soma2(5, 9)
print('----------------------------')
soma2(b=5, a=9)  # explicitar os parametros (pode inverter)
print('----------------------------')
contador(7, 8, 9, 10, 45)  # Desenpacota
contador(4, 5, 1)
print('----------------------------')
lista = [7, 5, 6, 4, 2]
dobra(lista)  # Dobra o valor da Lista
