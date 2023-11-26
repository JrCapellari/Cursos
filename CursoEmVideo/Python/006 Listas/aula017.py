lista = [2, 5, 9, 1]  # lista
print(lista)
lista[2] = 3  # substitui o valor
print(lista)
lista.append(7)  # adiciona valor ao final da lista
print(lista)
lista.sort()  # organiza os valores orden crescente
print(lista)
lista.sort(reverse=True)  # organiza os valores orden decresente
print(lista)
lista.insert(2, 0)  # na posição 2 inseriu o valor 0
print(lista)
lista.insert(2, 2)  # na posição 2 inseriu o valor 2
print(lista)
lista.remove(2)  # removeu o primeiro valor 2
print(lista)
lista.pop()  # elimina o último valor
print(lista)
lista.pop(2)  # elimina o valor no indice 2
print(lista)
if 4 in lista:
    lista.remove(4)
else:
    print('Numero 4 não encontrado')
print(f'Número de elementos: {len(lista)}')

# inserindo valores em lista vazia e formatando
valores = list()
valores.append(7)
valores.append(3)
valores.append(7)
for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores):
    print(f'indice {c} valor {v}')

'''num = list()
for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))
for c, v in enumerate(num):
    print(f'indice {c} valor {v}')'''

a = [2, 3, 4, 7]
b = a  # cria uma LIGAÇÃO entre as listas
b[2] = 8
print(a)
print(b)

c = [2, 3, 4, 7]
d = c[:]  # cria uma COPIA da lista C para D
d[2] = 8
print(c)
print(d)
