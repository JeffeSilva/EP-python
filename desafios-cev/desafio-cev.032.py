#!/usr/bin/env python
from datetime import date
ano = int(input('Informe um ano, caso queira usar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este é um ano Bissexto')
else:
    print('Não é um ano Bissexto')

