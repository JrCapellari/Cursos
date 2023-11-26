s1 = float(input('Medida do primeiro seguimento (cm): '))
s2 = float(input('Medida do segundo seguimento (cm): '))
s3 = float(input('Medida do terceiro seguimento (cm): '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Os seguimentos PODEM formar um triângulo')
else:
    print('Os seguimentos NÃO PODEM formam um triângulo')