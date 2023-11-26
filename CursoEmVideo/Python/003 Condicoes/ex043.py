altura = float(input('Qual a altura (m)? '))
peso = float(input('Qual o peso (Kg)? '))
IMC = peso / altura ** 2
print(f'IMC = {IMC:.2f}')
if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC <= 25:
    print('Peso Ideal')
elif 25 < IMC <= 30:  # elif IMC > 25 and IMC <= 30
    print('Sobrepeso')
elif 30 < IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
