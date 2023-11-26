from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input(f'Quando nasceu a {c}ª pessoa: '))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'{totmaior} pessoas são de MAIOR IDADE\n{totmenor} pessoas são de MENOR IDADE')
