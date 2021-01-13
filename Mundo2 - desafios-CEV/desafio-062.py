#!/usr/bin/env python
#ENTRADA DO USUARIO
num = int(input('Informe o 1° termo: '))
raz = int(input('Informe a razão da P.A: '))
#VARIAVEIS
c = 0
nl = 0
sair = 1
while c < 10:
    num += raz
    c += 1
    print(num)
    if sair == 1 and c == 10:
        while c != nl:
            num += raz
            c += 1
            print(num)
        nl = int(input('Quantos termos mais deseja imprimir: '))
    sair = int(input('Deseja continuar? SIM - (1), NÃO - (0)'))