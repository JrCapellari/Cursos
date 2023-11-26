n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print(f'Sua média é {media}')
if media >= 6.0:
    print('aprovado'.upper())
else:
    print('reprovado'.upper())
