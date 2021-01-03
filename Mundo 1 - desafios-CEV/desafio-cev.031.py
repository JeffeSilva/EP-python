#!/usr/bin/env python
dist = float(input('Informe a distancia em Km: '))
if dist <= 200:
    preco = 0.50
else:
    preco = 0.45
vdp = dist * preco
print('O valor da passagem é: R$ {:.2f}'.format(vdp))