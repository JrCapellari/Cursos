def ajuda(com):
    print(f'Acessando o manual do comando \'{com}\'')
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# PROGRAMA PRINCIPAl
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca: '))
    if comando in 'FIMfim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO')
