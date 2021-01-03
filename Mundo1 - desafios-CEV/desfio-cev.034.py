#!/usr/bin/env python
sal = float(input('Informe o salário do funcionario: '))
if sal >= 1250.00:
    sal = sal + (sal * 0.10)
    print(f'Valor do salário com aumento: R${sal}')
elif sal <= 1250.00:
    sal = sal + (sal * 0.15)
    print(f'Valor do salário com aumento: R${sal}')
else:
    print('Erro verifique e informe um valor valido')
