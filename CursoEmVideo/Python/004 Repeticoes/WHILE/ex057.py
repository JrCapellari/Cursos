'''s = '' # MINHA SOLUÇÃO
while s != 'M' and s != 'F':
    s = str(input('Digite o sexo M/F: ')).upper()[0].strip()
    if s != 'M' and s != 'F':
        print('Opção inválida, tente novamente')
print(f'Sexo ({s}) registrado'.upper())'''

# SOLUÇÃO CURSO EM VIDEO
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('DADO INVÁLIDO: Digite o sexo [M/F]: ')).strip().upper()[0]
print(f'Dado ({sexo}) iserido com SUCESSO')
