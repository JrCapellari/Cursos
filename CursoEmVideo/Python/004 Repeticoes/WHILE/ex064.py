num = cont = soma = 0
while num != 999:
        num = int(input('Digite um número para somar [999 para sair]: '))
        if num < 999:
            cont += 1
            soma += num
        else:
            print(f'Você digitou {cont} números e a soma é {soma}')
print('FIM')
