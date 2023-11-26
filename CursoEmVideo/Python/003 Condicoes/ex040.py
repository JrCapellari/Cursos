nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f'Sua média é {media:.2f} esta APROVADO')
elif media < 5.0:
    print(f'Sua méida é {media:.2f} esta REPROVADO')
else:
    print(f'Sua média é {media:.2f} esta em RECUPERAÇÃO')
