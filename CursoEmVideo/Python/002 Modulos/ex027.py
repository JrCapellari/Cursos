n = str(input('Digite seu nome: ')).strip().title()
print(f'Ola {n}')
nome = n.split()
# print(nome)
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[len(nome)-1]}')


