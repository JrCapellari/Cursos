pessoas = {'nome': 'Junior', 'sexo': 'M', 'idade': 44}
print(pessoas['nome'], pessoas['sexo'], pessoas['idade'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())  # somente as chaves
print(pessoas.values())  # somente os valores
print(pessoas.items())  # chaves e valores

print('\n-- estrutura com FOR --')
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k}: {v}')

print('\n-- deletado o ITEM sexo --')
del pessoas['sexo']  # deleta o ITEM (chave e valor)
for k, v in pessoas.items():
    print(f'{k}: {v}')

print('\n-- substituindo VALORES --')
pessoas['nome'], pessoas['idade'] = 'Leandro', 52  # substitui VALORES
for k, v in pessoas.items():
    print(f'{k}: {v}')

print('\n-- adicionando CHAVES e VALORES --')
pessoas['peso'], pessoas['sexo'] = 85, 'M'
for k, v in pessoas.items():
    print(f'{k}: {v}')

print('\n-- criando DICIONARIO dentro de LISTA --')
brasilsul = []
estado1 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
estado2 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
estado3 = {'uf': 'Paraná', 'sigla': 'PR'}
brasilsul.append(estado1)
brasilsul.append(estado2)
brasilsul.append(estado3)
print(estado1)  # mostra o dicionario solicitado
print(brasilsul)  # mostra a lista com todos os dicionarios
print(brasilsul[2])  # mostra o dicionario (indice 2) dentro da lista
print(brasilsul[1]['uf'])  # mostra o valor na chave UF do dicionario indice 1
print(brasilsul[0]['sigla'])  # mostra o valor na chave SIGLA do dicionario indice 0

print('\n-- solicitando dados ao usuário e fazendo copia')
brasil = list()
estado = dict()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip().title()
    estado['sigla'] = str(input('Sigla do estado: ')).strip().upper()
    brasil.append(estado.copy())
print(brasil)

print('\n-- mostrando valores com laços FOR')
for l in brasil:  # FOR da lista
    for v in l.values():
        print(f'{v}', end=' ')
