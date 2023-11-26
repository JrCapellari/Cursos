def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mERR0: Digite um número inteiro\033[m')
        if ok:
            break
    return valor


# PROGRAMA PRINCIPAL
n = leiaint('Digite um número: ')
print(f'Você digitou {n}')
