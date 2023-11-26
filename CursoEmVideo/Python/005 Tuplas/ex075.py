n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
numeros = (n1, n2, n3, n4)
print('Os números são ', end='')
for n in numeros:
    print(f'{n} ', end='')
print('\nOs valores pares são ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n} ', end='')
print(f'\nO 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O 3 aparece na {numeros.index(3) + 1}ª posição')
else:
    print(f'O número 3 não foi digitado')

