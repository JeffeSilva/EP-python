#!/usr/bin/env python
#Comptador randomiza um número de 0 a 5
from random import randint
vit = 0
soma = 0
vence = ''
#Repetição até o break
while True:
    #A randomização deve estar dentro do laço
    comp = randint(0, 10)
    #Usuario Escolhe entre Par ou Impar e entra com valor
    print('-=-' * 8)
    poui = str(input('Par ou Impar: [P/I]')).strip().upper()[0]
    num = int(input('Informe um número: '))
    print('-=-' * 8)
    print('')
    #Validações
    while poui not in 'PpiI':
        poui = str(input('Invalido verifique - [P/I]: ')).strip().upper()[0]
    #Logica do par ou Impar
    soma = comp + num
    if soma % 2 == 0:
        vence = 'Pp'
    else:
        vence = 'Ii'
    if poui in vence:
        print(f'Você venceu, computador {comp} o seu {num}. Denovo!\n')
        vit += 1
    else:
        print(f'Você perdeu, o valor que o computador escolheu foi {comp} o seu foi {num}. \n\nVocê venceu {vit} concecutivas.\n')
        break