#usr/bin/env python
#Entrada dos comprimentos de cada um dos lados do triangulo
r1 = int(input('Informe o valor de uma das retas: '))
r2 = int(input('Informe o valor da outra reta: '))
r3 = int(input('Informe o valor de mais uma reta: '))
# Aplicando principio do triangulo é verificando o seu tipo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel fazer um triangulo!')
    if r1 == r2 and r2 == r3:
        print('Este triangulo é Equilatero.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Este triangulo é isósceles.')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('Este triangulo é escaleno.')
else:
    print('Não é possivel fazer um triangulo')
