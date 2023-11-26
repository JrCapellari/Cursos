numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 20 >= num >= 0:
        break
    print('Número inválido.', end=' ')
for pos, cont in enumerate(numeros):
    if pos == num:
        print(f'O número digitado foi {numeros[pos]}')
print('fim')



