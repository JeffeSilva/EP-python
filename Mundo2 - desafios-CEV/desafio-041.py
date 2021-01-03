#!/usr/bin/env python
# Importação da biblioteca necessario para criar o programa
from datetime import date
# Entrada dos dados do usuario do programa
nome = str(input('Digite o nome do aluno: '))
ano = int(input('Informe o ano de nascimento do aluno {}: '.format(nome)))
idade = (date.today().year - ano)
# Condições e ordem de negocio
if idade <= 9:
     print('O aluno {} tem {} anos e esta classificado como mirim.'.format(nome, idade))
elif idade <= 14:
     print('O aluno {} tem {} anos e esta classificado como infantil.'.format(nome, idade))
elif idade <= 19:
    print('O aluno {} tem {} anos e esta classificado como junior.'.format(nome, idade))
elif idade <= 20:
    print('O aluno {} tem {} anos e esta classificado como sênior.'.format(nome, idade))
elif idade > 20:
    print('O aluno {} tem {} anos e esta classificado como master.'.format(nome, idade))
    