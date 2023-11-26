frase = str(input('Escreva uma frase: ')).strip()
minu = frase.lower()
print(f'A letra "a" aparece {minu.count("a")} vezes')
print(f'A primeira aparece na posição: {minu.find("a")+1}')
print(f'A última na posição: {minu.rfind("a")+1}')



