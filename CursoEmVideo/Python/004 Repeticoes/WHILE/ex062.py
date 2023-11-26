t1 = int(input('Primeiro termo da P.A: '))
r = int(input('Razão da P.A: '))
tn = int(input('Quantos termos terá a P.A?: '))
cont = 1
total = 0
nt = tn
while nt != 0:
    total += nt
    while cont <= total:
        print(f'{t1} ', end=' ')
        t1 += r
        cont += 1
    print('pause'.upper())
    nt = int(input('Quantos termos a mais deseja na P.A [0 para sair]: '))
print(f'fim da execução com {total} termos impressos'.upper())
