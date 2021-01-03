#!/usr/bin/env python
#import datetime
#Entrada dos anos, que o usuario nasceu e o ano atual
from datetime import date
ano = int(input('Informe o ano que você nasceu: '))
anoatual = date.today().year
#Condição, calculo de idade do usuario
if anoatual - ano == 18:
    print('Você deve se alistar este ano!')
elif anoatual - ano > 18:
    anosatraso = (anoatual - ano) - 18
    print('Você esta atrasado com seu alistamento em {} anos.'.format(anosatraso))
elif anoatual - ano < 18:
    anoadiantado = (ano - anoatual) + 18
    print('Você esta adiantado com seu alistamento em {} anos.'.format(anoadiantado))
else:
    print('Os dados inseridos são invalidos.')
print('O ano é: {}'.format(anoatual))
