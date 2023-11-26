pesoMaior = 0
pesoMenor = 0
for c in range(1, 6):
    peso = float(input(f'Qual o peso da {c}ª pessoa (Kg): '))
    if c == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print(f'O Maior peso é {pesoMaior}Kg\nO Menor peso é {pesoMenor}Kg')
