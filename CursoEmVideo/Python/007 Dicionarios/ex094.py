lista = []
soma = media = 0
while True:
    nome = str(input('Nome: ')).strip().title()
    sexo = str(input('Sexo: ')).strip().upper()[0]
    while sexo not in 'MmFf':
        print('ERRO: Digite apenas M ou F')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    soma += idade
    pessoas = {'nome': nome, 'sexo': sexo, 'idade': idade}
    lista.append(pessoas)
    s = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    while s not in 'SsNn':
        print('ERRO: Digite apenas S ou N')
        s = str(input('Continuar? [S/N]: '))
    if s in 'Nn':
        break
print(lista)
print(f'A) {len(lista)} pessoas foram cadastradas')
media = soma / len(lista)
print(f'B) A média das idades é: {media:.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=', ')
print(f'\nD) Pessoas com idade acima da média: ')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'   {k} = {v}', end=' ')
        print()

