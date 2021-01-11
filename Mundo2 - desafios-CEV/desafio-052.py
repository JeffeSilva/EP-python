#!/usr/bin/env python
print('')
print('{:=^35}'.format (' É ou não é primo! '))
print('')
num = int(input('Informe um número: '))
print('')
conte = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        conte += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=', ')
print('')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(num, conte))
if conte == 2:
    print('E o número {} é primo!.'.format(num))
else:
    print('O número {} não é primo!.'.format(num))
print('')
print('{:=^35}'.format (''))
print('')