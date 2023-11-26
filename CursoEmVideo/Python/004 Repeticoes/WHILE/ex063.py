nt = int(input('Quantos termos terá a sequencia Fibonacci? '))
cont = 0
t1 = 0
t2 = 1
print(f'{t1} {t2}', end=' ')
while cont <= nt:
    t3 = t1 + t2
    print(f'{t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1

