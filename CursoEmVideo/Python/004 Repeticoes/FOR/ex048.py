s = 0
c = 0
for m in range(1, 501, 2):
    if m % 3 == 0:
        c += 1  # contador
        s += m  # acumulador
print(f'{c}\n{s}')
