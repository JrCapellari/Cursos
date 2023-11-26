from random import randint
print('=' * 20)
print(' jogo par ou impar'.upper())
print('=' * 20)
cont = 0
while True:
    maqn = randint(0, 10)
    humn = int(input('Quantos dedos quer jogar?[0 a 10] '))
    pi = str(input('Quer PAR ou IMPAR?[P/I] ')).upper().strip()[0]
    total = maqn + humn
    if total % 2 == 0:
        r = 'P'
        re = 'PAR'
    else:
        r = 'I'
        re = 'IMPAR'
    print(f'Você {humn}\nComputador {maqn}\nTOTAL {total} {re}')
    if r == pi:
        print('=' * 12)
        print('Você venceu'.upper())
        print('=' * 12)
        cont += 1
    else:
        print('=' * 10)
        print('  perdeu'.upper())
        print('=' * 10)
        break
print('game over'.upper(), f'\nvocê venceu {cont} vezes')



