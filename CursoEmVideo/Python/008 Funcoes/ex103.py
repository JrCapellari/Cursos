def ficha(j='', g=''):
    if j in '':
        j = 'Desconhecido'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    print(f'O jogador {j} fez {g} gol(s) no campeonato')


# PROGRAMA PRINCIPAL
jog = str(input('Jogador: ')).strip().title()
gols = str(input('Gols: '))
ficha(jog, gols)
