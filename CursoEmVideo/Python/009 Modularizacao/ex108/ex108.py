import moeda

valor = float(input('Qual o preço? R$'))
print(f'Acrescimo de 10% {moeda.forma(moeda.aumentar(valor, 10))}')
print(f'Desconto de 10% {moeda.forma(moeda.diminuir(valor, 10))}')
print(f'O dobro de {moeda.forma(valor)} é {moeda.forma(moeda.dobro(valor))}')
print(f'A metade de {moeda.forma(valor)} é {moeda.forma(moeda.metade(valor))}')



