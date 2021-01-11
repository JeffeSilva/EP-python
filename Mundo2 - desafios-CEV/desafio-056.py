#!/usr/bin/env python
print('')
totalidade = 0
homemvelho = 0
nomevelho = ''
mulherjovem = 0
for c in range(1, 5):
    print('{:=^25}'.format (' {}ª Pessoa '.format(c)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    totalidade += idade
    if c == 1 and sexo == 'm' or sexo == 'M':
        homemvelho = idade
        nomevelho = nome
    if sexo == 'm' or sexo == 'M' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo == 'f' or sexo == 'F' and idade < 20:
        mulherjovem += 1
    print('')
midade = totalidade / 4
print('A média da idade do grupo é {}.'.format(midade))
print('No grupo tem {} mulheres com menos de 20 anos!'.format(mulherjovem))
print('O nome do homem mais velho é: {} e tem {} anos'.format(nomevelho, homemvelho))
  