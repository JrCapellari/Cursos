salarioAtual = float(input('Valor atual do salário: '))
if salarioAtual > 1250.00:
    aumento = salarioAtual * 0.10
else:
    aumento = salarioAtual * 0.15
salarioNovo = salarioAtual + aumento
print(f'Salário corrigido R${salarioNovo:.2f}')
print(f'Aumento de R${aumento:.2f}')
