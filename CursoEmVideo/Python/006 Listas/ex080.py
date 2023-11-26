num = []
for c in range(0, 5):
    n = int(input(f'Digite um número: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Add final lista')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Add na posição {pos}')
                break
            pos += 1
print(num)
