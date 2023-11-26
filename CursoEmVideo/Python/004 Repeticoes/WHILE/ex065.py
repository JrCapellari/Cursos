soma = num = cont = maior = menor = 0
sair = 'S'
while sair == 'S':
    num = float(input('Digite um número: '))
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    sair = str(input('Que continuar [S/N]? ')).upper().strip()[0]
    soma += num
    cont += 1
print(f'{cont} números digitados\nA soma é {soma} e a média é {soma/cont:.1f}'.upper())
print(f'O MAIOR número é {maior} e o MENOR é {menor}')

