import moeda

valor = float(input('Qual o preço? R$'))
print(f'A metade de R${valor} é R${moeda.metade(valor)}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'Acrescimo de 10% R${moeda.aumentar(valor, 10)}')
print(f'Desconto de 10% R${moeda.diminuir(valor, 10)}')
