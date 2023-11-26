jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gols
    jogador['total'] = sum(jogador['gols'])
print(f'-' * 30)
print(jogador)
for k, v in jogador.items():
    print(f'{k} tem valor {v}')
print(f'-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i + 1} fez {v} gols')
print(f'Totalizando: {jogador["total"]} gols')
