import math

catoposto = eval(input('Digite o cateto oposto: '))
catadjacente = eval(input('Digite o cateto adjacente: '))
#raiz = pow(catoposto, 2) + pow(catadjacente, 2)
#hipo = sqrt(raiz)
hipo = math.hypot(catoposto, catadjacente)
print(f'A hipotenusa é: {hipo:.2f}')
