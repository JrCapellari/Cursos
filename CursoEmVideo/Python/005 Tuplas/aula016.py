#  Tuplas      0          1        2        3           4      Tuplas são imutavéis
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudin', 'Batata Frita')
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[-4])
print(lanche[1:3])
print(lanche[:2])
print(lanche[1:])
print(lanche[:-3])
print(lanche[-1:])
print(len(lanche), 'Lanches')
for comida in lanche:
    print(f'Vou comer {comida}')
for cont in range(0, len(lanche)):
    print(lanche[cont])
for pos, comida in enumerate(lanche):
    print(f'{pos} Comer {comida}')
print(sorted(lanche))

a = (2, 5, 4)
print(f'Tupla a {a}')
b = (5, 8, 1, 2)
print(f'Tupla b {b}')
c = b + a
print(f'Tupla c = a + b {c}')
print(f'O 5 aparece {c.count(5)} vezes')
print(f'A posição de 8 é {c.index(8)}')

pessoa = ('Junior', 44, 'M', 1.65, 86)
print(pessoa)
