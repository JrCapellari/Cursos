frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letras in range(len(juntar) - 1, -1, -1):
    inverso += juntar[letras]
print(f'{juntar} {inverso}')
if inverso == juntar:
    print('palíndromo'.upper())