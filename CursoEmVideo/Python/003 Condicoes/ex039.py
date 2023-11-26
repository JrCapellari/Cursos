from datetime import date
ano_nasc = int(input('Digite o ano de seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade < 18:
    print(f'Você tem {idade} anos\nFaltam {18 - idade} anos para você se alistar')
elif idade == 18:
    print(f'Você tem {idade} anos\nCompareça imediatamente a junta de alistamento')
else:
    print(f'Você tem {idade} anos\npassaram-se {idade - 18} anos para o alistamento\nCaso não efetuado compareça a uma junta')
