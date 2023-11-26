from random import randint
from time import sleep
print('=' * 35)
print('        adivinhe o número'.upper())
print('=' * 35)
print('Vou escolher um número entre 0 e 5')
aleatorio = randint(0, 5)
sleep(2)
print('pronto'.upper())
acertou = False
p = 0
while not acertou:
    num = int(input('Qual número escolhi: '))
    p += 1
    if num == aleatorio:
        acertou = True
    else:
        if num < aleatorio:
            print('ERROU - Dica: Número maior')
        elif num > aleatorio:
            print('ERROU - Dica: Número menor')
print('correto'.upper())
print(f'Você tentou {p} vezes ate acertar')
