#!/usr/bin/env python
print('{:=^40}'.format (' Somente N° Pares de 1 até 50 '))
for c in range(1, 50+1):
    print('.', end='')   
    if c % 2 == 0:
        print(c, end=' ')
print('{:=^40}'.format(' Fim '))

#OTIMIZANDO EXERCICIO
print('{:=^40}'.format (' Otimizado '))
for cont in range(2, 51, 2):
    print('.', end=' ')
    print(cont, end=' ')
print('{:=^40}'.format (' FIM '))

# IMPORTANTE OBSERVAR QUE A DEPENDER DA SOLIÇÃO DO PROBLEMA ELA PODE NÃO SER A MAIS EFICIENTE. PRIORIZE - 1° SOLUCIONAR O PROBLEMA, 2° OTIMIZE A SOLUÇÃO PARA ESTE PROBLEMA, NÃO DA PRA OTIMIZAR. SOLUCIONADO ESTA!