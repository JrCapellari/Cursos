idadeTotal = 0
idadeMaior = 0
nomeVelho = ''
totMulher = 0
for c in range(1, 5):
    print(f'---- {c}ª PESSOA ----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '.strip()))
    sexo = str(input('Sexo[F/M]: ')).strip().upper()
    idadeTotal += idade
    if c == 1 and sexo == 'M':
        idadeMaior = idade
        nomeVelho = nome
    if sexo == 'M' and idade > idadeMaior:
        idadeMaior = idade
        nomeVelho = nome
    if sexo == 'F' and totMulher < 20:
        totMulher += 1
print('--------------------------------------------')
print(f'A média de idade do grupo é: {idadeTotal/c:.2f} anos')
print(f'O homem mais velho tem {idadeMaior} anos e se chama {nomeVelho}')
print(f'Neste grupo existem {totMulher} mulheres com menos de 20 anos')