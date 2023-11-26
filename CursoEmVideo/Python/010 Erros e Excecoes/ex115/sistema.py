from libr.minhaUI import *
from libr.arquivo import *
from time import sleep


arq = 'E:Cursos/CursoEmVideo/PYTHON/010 erros e excecoes/ex115/dados.txt'
if not arqexiste(arq):
    criararquivo(arq)

while True:
    resp = menu(['listar cadastro', 'cadastrar pessoas', 'sair'])
    if resp == 1:
        # lista o cadastro
        cabeca('LISTA DE PESSOAS')
        lerarquivo(arq)
    elif resp == 2:
        # cadastra nova pessoa
        cabeca('NOVO CADASTRO')
        nome = str(input('Digite o nome: '))
        idade = leiaint('Digite a idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print(f'Fechando aplicação....')
        sleep(1)
        print('encerrado'.upper())
        break
    else:
        print('\33[31m:::ERRO::: opção inválida\33[m')
