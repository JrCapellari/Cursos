'''from math import factorial
num = int(input('Calcule o fatorial de: '))
fatorial = factorial(num)
print(f'O fatorial de {num}! é {fatorial}')'''

num = int(input('Calcule o fatorial de: '))
c = num
f = 1
while c > 0:
    print(c, end = ' ')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f'{num}! = {f}')



