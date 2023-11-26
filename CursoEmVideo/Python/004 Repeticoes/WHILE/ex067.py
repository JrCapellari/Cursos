while True:
    print('=' * 27)
    num = int(input('Qual tabuada deseja ver? '))
    print('=' * 27)
    if num < 0:
        break
    for c in range(1, 11):
        r = num * c
        print(f'{num} X {c} = {r}')
print('execução encerrada'.upper())
