nome = str(input('Digite seu nome: ')).strip()
print(f'Ola {nome.title()}')
print(f'Ola {nome.lower()}')
print(f'Ola {nome.upper()}')
print(f'Seu nome tem', len(nome) - nome.count(' '), 'letras')
print(f'Seu primeiro nome tem', nome.find(' '), 'letras')
separa = nome.split()
print(f'{separa}')
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')




