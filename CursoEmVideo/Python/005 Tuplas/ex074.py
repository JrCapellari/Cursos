from random import randint
ale = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores são: ', end='')
for n in ale:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi: {max(ale)}')
print(f'O menor valor sorteado foi: {min(ale)}')
