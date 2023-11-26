p = 0
s = 0
for c in range(1, 7):
    n = int(input(f'Escolha o {c}º numero: '))
    if n % 2 == 0:
        p += 1
        s += n
print(f'Foram informados {p} números pares\nA soma entre eles é {s}')

