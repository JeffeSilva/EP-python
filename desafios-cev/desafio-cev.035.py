#usr/bin/env python
r1 = int(input('Informe o valor de uma das retas: '))
r2 = int(input('Informe o valor da outra reta: '))
r3 = int(input('Informe o valor de mais uma reta: '))
if r3 - r1 < r2 < r3 + r2 and r3 - r2 < r1 < r3 + r2 and r2 - r1 < r3 < r2 + r1:
    print('É possivel fazer um triangulo!')
else:
    print('Não é possivel fazer um triangulo')