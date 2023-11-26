n1 = eval(input('Digite um numero '))
n2 = eval(input('Digite outro numero '))
som = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
pot = n1 ** n2
mod = n1 % n2
print(f'a soma é {som} a subtração é {sub} a multiplicação é {mul}', end='')
print(f' a divisão é {div:.2f} a potencia é {pot} o modulo {mod}')
