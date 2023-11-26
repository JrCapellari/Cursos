nome = str(input('Qual seu nome: ')).strip().title()
if nome == 'Junior':
    print(f'Ola {nome}, realmente esse é seu nome')
elif nome == 'Rose' or nome == 'Dyandra' or nome == 'Pandora':
    print(f'Ola {nome}, seu nome é muito bonito')
elif nome in 'Paulo Pedro Ricardo Maria Ana':
    print(f'{nome}, Seu nome esta na lista')
else:
    print('Outro nome')
print('Boa Tarde!!')
