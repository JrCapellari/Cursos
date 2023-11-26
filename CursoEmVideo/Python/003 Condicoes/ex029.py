vel = float(input('Velocidade do veículo (km/h): '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'Limite 80 Km/h\n'
          f'Sua velocidade {vel} Km/h\n'
          f'Excedido em {vel - 80} Km/h\n'
          f'Valor da multa R${multa:.2f}')
else:
    print('Velocidade permitida')
