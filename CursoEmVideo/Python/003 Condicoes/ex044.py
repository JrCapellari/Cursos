print(f'===== LOJAS TABAJARA =====')
valor = float(input('Valor do produto R$ '))
print(f'''ESCOLHA FORMA DE PAGAMENTO
Digite (1) para DINHEIRO / PIX
Digite (2) para DÉBITO
Digite (3) para CRÉDITO''')  # 3 aspas varias linhas
cond = int(input('Digite a opção: '.upper()))

if cond == 1:
    print('DINHEIRO / PIX')
    desc = int(input('Porcentagem de desconto: '))
    valor = valor - (valor * desc / 100)
    print(f'{desc}% de desconto\nValor a pagar R$ {valor:.2f}')
elif cond == 2:
    print('DÉBITO')
    desc = int(input('Porcentagem de desconto: '))
    valor = valor - (valor * desc / 100)
    print(f'{desc}% de desconto\nValor a pagar R$ {valor:.2f}')
elif cond == 3:
    print('CRÉDITO')
    parc = int(input('Número de parcelas: '))
    if parc == 1 or parc == 2:
        total = valor
        valor = valor / parc
        print(f'{parc}X de {valor:.2f} sem juros\nTotal R$ {total:.2f}')
    elif parc >= 3 and parc <= 6:
        print('::: ATENÇÃO :::\nValor acrescido de 20%')
        valor = valor + (valor * 20 / 100)
        total = valor
        valor = valor / parc
        print(f'{parc}X de {valor:.2f} com juros\nTotal R$ {total:.2f} ')
    else:
        print('Opção de parcelas INVÁLIDA\nTente Novamente')
else:
    print(f'Opção {cond} INVÁLIDA, tente novamente')

print('Gratos pela preferencia')
