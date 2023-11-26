km = eval(input('Kilometros percorridos: '))
dias = int(input('Dias alugados: '))
total = (dias * 60) + (km * 0.15)
print(f'Valor a pagar pelo aluguel do veiculo R$ {total:.2f}')
