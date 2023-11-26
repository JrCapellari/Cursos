from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = {}
# preenchendo o dicionario (jogo)
for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)
    c += 1
# mostrando o jogo
print('---- jogando o dado ----'.upper())
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
# mostrando os vencedores em orden decrecente
print('------- Ranking --------'.upper())
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
