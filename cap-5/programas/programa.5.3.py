#!/usr/bin/env python
# Tabuada de adição deve ser impressa de 1 a 10 sendo n o número digitado pelo usuario.
n = int(input('Tabuada de: '))
x = 1
while x <= 10:
    print('{} + {} = '.format(n, x,), n + x)
    x = x + 1
print('FIM ')