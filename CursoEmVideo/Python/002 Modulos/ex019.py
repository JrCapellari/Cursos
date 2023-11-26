from random import choice

n1 = input('Nome do aluno: ')
n2 = input('Nome do aluno: ')
n3 = input('Nome do aluno: ')
n4 = input('Nome do aluno: ')

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O escolhido é {escolhido}')
