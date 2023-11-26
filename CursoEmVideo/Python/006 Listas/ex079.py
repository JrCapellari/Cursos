num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
    else:
        print(f'{n} já existe, não será adicionado')
    s = ' '
    while s not in 'SsNn':
        s = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if s in 'Nn':
        break
print(f'Você digitou {sorted(num)}')
