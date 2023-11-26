import uteis_pacote


num = int(input('Digite um número: '))
fat = uteis_pacote.fatorial(num)
print(f'{num}! = {fat}')
print(f'O dobro de {num} é {uteis_pacote.dobro(num)}')
print(f'O triplo de {num} é {uteis_pacote.triplo(num)}')
