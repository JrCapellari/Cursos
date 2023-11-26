grupo = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        grupo[0].append(num)
    if num % 2 == 1:
        grupo[1].append(num)
print(f'GRUPO: {grupo}')
print(f'PARES: {sorted(grupo[0])}')
print(f'IMPARES: {sorted(grupo[1])}')
