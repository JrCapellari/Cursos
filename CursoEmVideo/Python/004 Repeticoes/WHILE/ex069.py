cont = idmaior = sexmasc = idmenor = 0
while True:
    print('-' * 15)
    print('cadastro e pessoas'.upper())
    print('-' * 15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    cont += 1
    if idade >= 18:
        idmaior += 1
    if sexo in 'Mm':
        sexmasc += 1
    if idade < 20 and sexo in 'Ff':
        idmenor += 1
    if sair in 'Nn':
        break
print('-' * 20)
print(f'{cont} Pessoas cadastradas')
print(f'{idmaior} Pessoas acima de 18 anos')
print(f'{sexmasc} Homens cadastrados')
print(f'{idmenor} Mulheres com menos de 20 anos')
print('-' * 20)

