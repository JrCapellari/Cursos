from datetime import date
dta_atual = date.today().year
ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = dta_atual - ano_nasc
if idade <= 9:
    print(f'O atleta tem {idade} anos\nCategoria: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos\nCategoria: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos\nCategoria: JÚNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos\nCategoria: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos\nCategoria: MASTER')
