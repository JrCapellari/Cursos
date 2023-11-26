pessoa = []
grupo = []
while True:
    nome = str(input('Digite o nome: ')).strip().title()
    peso = float(input('Digite o peso [Kg]: '))
    pessoa.append(nome)
    pessoa.append(peso)
    grupo.append(pessoa[:])
    pessoa.clear()
    s = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    while s not in 'SsNn':
        s = str(input('Opção inválida. Continuar? [S/N]: ')).strip().upper()[0]
    if s in 'Nn':
        break
print(grupo)
print(f'{len(grupo)} pessoas foram cadastradas')
maiorp = menorp = 0
for p in grupo:
    if p[1] >= maiorp:
        maiorp = p[1]
    if p[1] < maiorp:
        menorp = p[1]
print(f'O MAIOR peso foi {maiorp}:', end=' ')
for p in grupo:
    if p[1] == maiorp:
        print(f'{p[0]}', end=' ')
print(f'\nO MENOR peso foi {menorp}:', end=' ')
for p in grupo:
    if p[1] == menorp:
        print(f'{p[0]}', end=' ')

