#!/usr/bin/env python
from time import sleep
#Variaveis
ci = 0
chc = 0
mcmv = 0
sair = ''
while True:
    #Entrada Usuario
    print('-=-' * 10)
    sexo = str(input('Informe o sexo - [M/F]: ')).upper().strip()
    idade = int(input('Informe a idade: '))
    print('-=-' * 10)
    #Verificação continuar ou não
    sair = str(input('Deseja continuar? - [S/N]:')).upper().strip()
    #Logica do programa
    if idade > 18:
        ci += 1
    if sexo in 'Mm':
        chc += 1
    if sexo in 'Ff' and idade < 20:
        mcmv += 1
    if sair in 'S':
        print('PROCESSANDO...')
        sleep(2)
        break
print('')
print(f'{ci} pessoas tem mais de 18 anos \n{chc} Homens foram cadastrados \n{mcmv} Mulheres tem menor de 20 anos')
print('')
print('Fim')
