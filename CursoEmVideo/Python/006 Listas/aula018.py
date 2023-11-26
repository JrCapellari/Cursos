teste = []
teste.append('Gustavo')
teste.append(40)
# print(teste)

galera = []
galera.append(teste[:])  # [:] faz uma copia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  # [:] faz uma copia
# print(galera)
lista = []

grupo = [['junior', 44], ['Rose', 42], ['Dyandra', 23], ['Pandora', 12], ['Akira', 6]]
print(grupo[4][0], grupo[1][1])
for p in grupo:
    print(f'{p[0]} tem {p[1]} anos')

'''pessoas = []
dados = []
totmai = totmen = 0
for c in range(0, 5):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))
    pessoas.append(dados[:])  # [:] faz uma copia
    dados.clear()
print(pessoas)
for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} menor de idade')
        totmen += 1
print(f'{totmai} pessoas são maiores e {totmen} pessoas são menores de idade')'''
