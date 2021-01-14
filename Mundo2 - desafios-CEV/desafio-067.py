#!/usr/bin/env python
from time import sleep
while True:
    c = 1
    print('-=-' * 10)
    num = int(input('Qual tabuada você deseja?: '))
    print('-=-' * 10)
    if num < 0:
        print('')
        print('FINALIZANDO...')
        print('')
        sleep(2)
        print('Volte sempre!')
        print('')
        break
    else:
        while c < 11:
            res = num * c
            print(f'{num} x {c} = {res}')
            c += 1
print('FIM ')