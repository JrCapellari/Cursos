print('-' * 20)
print('loja super baratão'.upper())
print('-' * 20)
cont = total = valormaior = valormenor = 0
while True:
    nome = str(input('Nome do produto: ')).strip()
    valor = float(input('Valor R$ '))
    cont += 1
    total += valor
    if cont == 1:
        valormaior = valormenor = valor
    if valor > valormaior:
        valormaior = valor
    if valor < valormenor:
        valormenor = valor
        nomeprod = nome
    if valor > 1000.00:
        prod = cont
    sair = ' '
    while sair not in 'SsNn':
        sair = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if sair in 'Nn':
        break
print(f'{cont} produtos comprados')
print(f'Total de R$ {total:.2f} Reais')
print(f'{prod} produtos acima de R$ 1000,00')
print(f'O maior valor é R$ {valormaior:.2f} Reais')
print(f'O produto {nomeprod} tem o menor valor - R$ {valormenor:.2f} Reais')
