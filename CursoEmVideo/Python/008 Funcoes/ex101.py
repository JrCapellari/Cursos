def voto(ano):
    from datetime import date
    atual = date.today().year
    i = atual - ano
    if i < 16:
        return f'Idade {i} anos: Não pode VOTAR'
    elif 16 <= i < 18 or i > 65:
        return f'Idade {i} anos: Voto Opcional'
    else:
        return f'Idade {i} anos: Pode VOTAR'


# PROGRAMA PRINCIPAL
ano_nasc = int(input('Digite o ano de nascimento: '))
print(f'{voto(ano_nasc)}')
