times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
         'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo',
         'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
         'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(f'Classificação: {times}')
print(f'Os 5 primeiros: {times[0:5]}')
print(f'Os 4 últimos: {times[-4:]}')
print(f'Ordem alfabética: {sorted(times)}')
print(f'O São Paulo esta na posição {times.index("São Paulo")+1}ª')
