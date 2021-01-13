#!/usr/bin/env python
sair = 0
somar = 0
c = 1
while sair != 999:
    num = int(input('Digite números para somar, ou [999] para sair: '))
    if num == 999:
        sair = 999
    if num != 999:
        somar += num
        c += 1       
print('Foram digitados {} números e a soma é: {}.'.format(c - 1, somar))
