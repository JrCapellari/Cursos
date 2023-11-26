matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0
for l in range(0, 3):  # linha
    for c in range(0, 3):  # coluna
        matriz[l][c] = int(input(f'Digite um valor para {[l, c]}: '))
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
        if matriz[l][c] % 2 == 0:  # verificando se é par
            spar += matriz[l][c]
    print()  # para pular a linha da Matriz
print(f'Soma dos pares da matriz: {spar}')
# Somando a 3ª coluna
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma da 3ª coluna é: {scol}')
#  descobrindo o maior valor na 2ª linha
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número na 2ª linha é: {maior}')
