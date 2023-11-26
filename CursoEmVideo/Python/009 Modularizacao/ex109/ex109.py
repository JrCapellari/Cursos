import moeda

valor = float(input('Qual o preço? R$'))
print(f'Acrescimo de 10% {moeda.aumentar(valor, 10, True)}')
print(f'Desconto de 10% {moeda.diminuir(valor, 10, True)}')
print(f'O dobro de {moeda.forma(valor)} é {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.forma(valor)} é {moeda.metade(valor, True)}')



