sal = eval(input('Salario base R$ '))
porc = eval(input('Porcentagem de rajuste '))
rej = sal * porc / 100
print(f'Reajuste de R$ {rej} reais\nNovo salário R$ {sal + rej}\nPorcentagem {porc}%')
