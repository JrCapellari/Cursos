from random import randint
from time import sleep
print('-=-' * 12)
print('      JOGO ADIVINHE O NÚMERO')
print('-=-' * 12)
ale = randint(0, 5)
print(f'Vou pensar em um número entre 0 e 5')
sleep(3)
print('pronto'.upper())
num = int(input('Tente adivinhar qual número pensei: '))
if ale == num:
    print(f'Você ACERTOU parabens!!!')
else:
    print(f'ERROU, o numero escolhido era {ale}\nTente novamente')
