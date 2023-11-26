aluno = {}
aluno['nome'] = str(input('Nome do aluno: ')).strip().title()
aluno['nota'] = float(input(f'Nota de {aluno["nome"]} é: '))
if aluno['nota'] < 5:
    aluno['status'] = 'reprovado'.upper()
elif 5 <= aluno['nota'] < 7:
    aluno['status'] = 'recuperação'.upper()
else:
    aluno['status'] = 'aprovado'.upper()
# print(aluno)
print(f'{aluno["nome"]} obteve nota {aluno["nota"]:.2f} e esta {aluno["status"]}')
print('-' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
