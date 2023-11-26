num = int(input('Digite o número: '))
print('Escolha uma opção')
print('(1) binario'.upper())
print('(2) octa'.upper())
print('(3) hexadecimal'.upper())
base = int(input('Digite: '))
if base == 1:
    print(f'O Binário de {num} é {bin(num) [2:]}')
elif base == 2:
    print(f'O Octa de {num} é {oct(num) [2:]}')
elif base == 3:
    print(f'O Hexadecimal de {num} é {hex(num) [2:]}')
else:
    print('Opção invalida')
