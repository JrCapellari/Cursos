from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input('Quantos sorteios quer fazer: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1

# print(f'números sorteados: {sorted(jogos)}')
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1} = {sorted(l)}')

