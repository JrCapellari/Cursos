try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f':::Erro::: Digite apenas números inteiros')
except ZeroDivisionError:
    print(f':::Erro::: Denominador deve ser maior que "0"')
except KeyboardInterrupt:
    print('\nO programa parou')
except Exception as erro:
    print(f'Erro: {erro.__cause__}')
else:  # opcional
    print(f'O resultado é {r:.2f}')
finally:  # opcional
    print('obrigado!')
