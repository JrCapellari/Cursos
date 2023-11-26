from datetime import date
atual = date.today().year
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = atual - nasc
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Valor do salário R$ '))
else:
    dados['CTPS'] = 'não possui'
dados['aposentadoria'] = dados['contratação'] + 35
print(f'----- Dados -----')
# print(dados)
for k, v in dados.items():
    print(f'{k}: {v}')
