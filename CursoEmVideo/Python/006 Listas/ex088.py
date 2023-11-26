lista = []
while True:
    nome = str(input('Nome do aluno(a): ')).strip().title()
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    s = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while s not in 'SsNn':
        s = str(input('Valor inválido. Continuar? [S/N]: ').strip().upper()[0])
    if s in 'Nn':
        break
print('-' * 30)
print(f'{"Nº":<4} {"Nome":<10} {"Média":>8}')
print('-' * 30)
for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Notas de qual aluno? [999]: '))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f'As notas de {lista[opc][0]} são {lista[opc][1]}')
print('finalizado'.upper())
