a = []
b = []
c = []
while True:
    a.append(int(input('Digite um número: ')))
    s = str(input('Continuar? [S/N]:')).strip().upper()[0]
    while s not in 'SsNn':
        s = str(input('Valor inválido. Continuar? [S/N]: ')).strip().upper()[0]
    if s in 'Nn':
        break
for p in a:
    if p % 2 == 0:
        b.append(p)
    elif p % 2 != 0:
        c.append(p)
print(f'Lista completa: {a}')
print(f'Lista dos pares: {b}')
print(f'Lista dos impares: {c}')
