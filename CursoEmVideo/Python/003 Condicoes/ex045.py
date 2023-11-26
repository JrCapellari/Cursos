from random import randint
print('======= JOKEPÔ =======')
lista = ['pedra', 'papel', 'tesoura']
maquina = randint(0, 2)

print('''Suas opções
(0) PEDRA
(1) PAPEL
(2) TESOURA''')  # 3 asteriscos, varias linhas
usuario = int(input('Faça sua Jogada: '))
try:
    print(f'Você: {lista[usuario].upper()}')
except IndexError:
    print('opção invalida'.upper())
    
print(f'Oponente: {lista[maquina].upper()}')

if (usuario == 0 and maquina == 2) or (usuario == 1 and maquina == 0) or (usuario == 2 and maquina == 1):
    print('você ganhou'.upper())
elif (maquina == 0 and usuario == 2) or (maquina == 1 and usuario == 0) or (maquina == 2 and usuario == 1):
    print('você perdeu'.upper())
else:
    print('empate'.upper())
