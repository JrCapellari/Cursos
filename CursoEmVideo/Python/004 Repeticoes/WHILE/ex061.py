t1 = int(input('Primeiro termo da P.A: '))
r = int(input('Razão da P.A: '))
tn = int(input('Quantos termos terá a P.A?: '))
cont = 1
while cont <= tn:
    print(f'{t1} ', end='')
    t1 += r
    cont += 1
