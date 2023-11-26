distancia = float(input('Qual a distancia (Km) de sua viagem? '))
if distancia <= 200:
    print(f'Sua viagem custará R$ {distancia * 0.50:.2f}')
else:
    print(f'Sua viagem custará R$ {distancia * 0.45:.2f}')
print('Boa Viagem!!')