#usr/bin/env python
#Entrada dos comprimentos de cada um dos lados do triangulo
r1 = float (input('Informe o valor de uma das retas: '))
r2 = float (input('Informe o valor da outra reta: '))
r3 = float (input('Informe o valor de mais uma reta: '))
# Aplicando principio do triangulo é verificando o seu tipo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel fazer um triangulo!')
    if r1 == r2 and r2 == r3:
        print('Este triangulo é EQUILATERO.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Este triangulo é ISÓSCELES.')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('Este triangulo é ESCALENO!.')
else:
    print('Não é possivel fazer um triangulo')
