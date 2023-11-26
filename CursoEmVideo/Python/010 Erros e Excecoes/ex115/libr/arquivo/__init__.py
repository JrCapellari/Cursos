def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\33[31m:::ERRO::: Arquivo NÃO criado\33[m')
    else:
        print(f'Arquivo criado com sucesso')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(':::ERRO::: Algo aconteceu')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(':::ERRO::: algo aconteceu')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(':::ERRO::: algo aconteceu')
        else:
            print(f'Registro de {nome} adicionado com sucesso')
            a.close()
