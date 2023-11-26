frase = 'Curso em Video Python'
frase.strip()  # remove espaços do inicio e fim
print(frase)
print(f'{frase[9:]}')
print(len(frase))  # conta incluindo os espaços
print(frase.count('o'))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
print('-'.join(frase))
