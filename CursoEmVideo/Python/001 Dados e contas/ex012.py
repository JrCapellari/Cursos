valor = eval(input('valor da compra R$ '))
desc = eval(input('porcentagem de desconto % '))
porc = valor * desc / 100
print(f'Seu desconto é R$ {porc} Reais você vai pagar R$ {valor - porc} Reais')

