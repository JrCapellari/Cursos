import math

angulo = eval(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'Ângulo {angulo}\nSeno {seno:.2f}\nCosseno {cosseno:.2f}\nTangente {tangente:.2f}')
