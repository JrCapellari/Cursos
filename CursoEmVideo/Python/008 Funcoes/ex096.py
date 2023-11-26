def area(l, c):
    a = l * c
    print(f'A area de um terreno de {l:.2f}m X {c:.2f}m é {a:.2f}m²')


# PROGRAMA PRINCIPAL
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

