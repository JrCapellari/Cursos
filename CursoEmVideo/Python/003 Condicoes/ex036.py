valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
parcelas = int(input('Em quantas parcelas mensais deseja pagar? '))

valor_parcela = valor_casa / parcelas
salario30 = salario * 0.30
if valor_parcela > salario30:
    print('Valor da parcela excede 30% do salario')
else:
    print('Parabens, emprestimo aprovado')