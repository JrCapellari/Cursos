jogador = {}
gols = []
time = []
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'- Quantos gols na partida {c}? ')))
        jogador['gols'] = gols[:]
        jogador['total'] = sum(jogador['gols'])
    s = str(input('Continuar? [S/N] ')).upper().strip()[0]
    while s not in 'SsNn':
        print('ERRO: Dgite apenas S ou N')
        s = str(input('Continuar? [S/N] ')).upper().strip()[0]
    gols.clear()
    time.append(jogador.copy())
    if s in 'Nn':
        break
print(f'-' * 40)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(f'-' * 40)
while True:
    busca = int(input('Mostrar dados do jogador, digite o cod ou 999 para sair: '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO: codigo não existe')
    else:
        print(f'DADOS do JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'- No jogo {i + 1} fez {g} gols')
print('FINALIZADO')
