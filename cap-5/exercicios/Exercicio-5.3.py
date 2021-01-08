#usr/bin/env python
# Exercicio 5.3 - Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ....,1, 0 e FOGO!
from time import sleep
cont = 10
while cont >= 0:
    print(cont), sleep(1)
    cont = cont - 1
print(' FOGO ! ')
print(' FIM ')