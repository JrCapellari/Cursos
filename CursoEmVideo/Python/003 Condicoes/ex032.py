from datetime import date
ano: int = int(input('Digite um ano ou insira "0" para ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é Bissexto')
else:
    print(f'{ano} não é Bissexto')

''' Forma aninhada
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'{ano} é bissexto')
        else:
            print(f'{ano} não é bissexo')
    else:
        print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')'''
