produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32,
            'Canetas', 22.30, 'Livro', 34.90)
print('-' * 30)
print(f'{"Listagem de Preços":^28}'.upper())
print('-' * 30)
for cont in range(0, len(produtos)):
    if cont % 2 == 0:
        print(f'{produtos[cont]:.<20}', end='R$ ')
    elif cont % 2 == 1:
        print(f'{produtos[cont]:>6.2f}')
print('-' * 30)
