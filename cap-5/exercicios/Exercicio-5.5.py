#!/usr/bin/env python
# Reescreva o programa anterior para escrever os 10 primeiros multiplos de 3.
c = 0
while c <= 60:
    if c % 3 == 0 and c % 2 == 1:
        print('.', end=' ')
        print(c)
    c = c + 1
print('FIM ')