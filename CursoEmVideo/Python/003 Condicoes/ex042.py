s1 = float(input('Digite o primeiro seguimento (cm): '))
s2 = float(input('Digite o segundo seguimento (cm): '))
s3 = float(input('Digite o terceiro seguimento (cm): '))
veriTri = s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1
if veriTri == True:
    print('Forma um triângulo? SIM')
    if s1 == s2 == s3:
        print('Tipo do triândulo: EQUILATERO')
    elif s1 != s2 != s3 != s1:  #  por ser difrença é nescessário avaliar todas as possibilidades
        print('Tipo do triãngulo: ESCALENO')
    elif s1 == s2 or s2 == s3 or s3 == s1:  # poderia usar apenas else
        print('Tipo do triângulo: ISÓCELES')
else:
    print('Forma um triângulo? NÃO\nReveja as medidas dos seguimentos')
