lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    s = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    while s not in 'SsNm':
        s = str(input('Opção invalida. Continuar? [S/N]: ')).strip().upper()[0]
    if s in 'Nn':
        break
lista.sort(reverse=True)
print(f'{len(lista)} números foram digitados')
print(f'Os números em orden descrecente foram {lista}')
if 5 in lista:
    print(f'O número 5 faz parte da lista')
else:
    print(f'O número 5 não foi encontrado na lista')
