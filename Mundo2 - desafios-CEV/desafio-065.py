#!/usr/bin/env python
from time import sleep
#variaveis
sair = 'N'
maior = 0
menor = 0
soma = 0
c = 0
while sair != 'S':
    #Entrada do Usuario
    num = int(input('Informe um valor: '))
    sair = str(input('Deseja sair?: [S/N]')).upper().strip()[0]
    c += 1
    #Qual maior?
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    #SOMA para tirar a media
    soma += num
media = soma / c
print('')
print('PROCESSANDO...'), sleep(2)
print('')
print('O maior valor é: {} \nO menor valor é: {} \nForam digitados {} valores. \nA soma de todos esses valores é: {} \nE a media geral é: {}'.format(maior, menor, c, soma, media))
print('')
print('FIM')
