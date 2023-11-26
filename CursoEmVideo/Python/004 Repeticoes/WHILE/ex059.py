num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
op = 0
while op != 5:
    print('=' * 26)
    print('        operações'.upper())
    # print('=' * 26)
    op = int(input('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    escolha a operação: '''.upper()))
    if op == 1:
        res = num1 + num2
        print(f'====== A soma é {res} ======'.upper())
    elif op == 2:
        res = num1 * num2
        print(f'====== A multiplicação é {res} ======'.upper())
    elif op == 3:
        if num1 > num2:
            print(f'====== O maior é {num1} ======'.upper())
        elif num1 < num2:
            print(f'====== O maior é {num2} ======'.upper())
        else:
            print('====== números iguais ======'.upper())
    elif op == 4:
        print('*** informe novos números ***'.upper())
        num1 = float(input('Primeiro número: '))
        num2 = float(input('Segundo número: '))
    elif op > 5 or op == 0:
        print('***** opção inválida *****'.upper())
print('\n***** programa encerrado *****'.upper())




