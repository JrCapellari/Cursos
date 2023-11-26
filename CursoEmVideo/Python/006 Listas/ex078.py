lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {cont}: ')))
    cont += 1
print(f'Você digitou os valores: {lista}')
print(f'O MAIOR valor foi {max(lista)} e esta na posição ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}, ', end='')
print(f'\nO MENOR valor foi {min(lista)} e esta na posição ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}, ', end='')
