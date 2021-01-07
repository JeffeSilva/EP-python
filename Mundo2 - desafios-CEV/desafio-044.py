#!/usr/bin/env python
# Entrada do usuario
from time import sleep
print(' ')
vdp = float(input('Informe o valor do produto: '))
vsd = vdp
print(' ')
#Menu com as opções que o usuario pode escolher!
print(' -=-=-=-=-=-=-=-=-=-=-=-=-Condições-=-=-=-=-=-=-=-=-=-=-=-=-=- \n')
print(' -=- (1) A vista em dinheiro/cheque: 10% de desconto       -=- ')
print(' -=- (2) A vista no cartão: 5% de desconto                 -=- ')
print(' -=- (3) Até duas vezes no cartão: Preço normal do produto -=- ')
print(' -=- (4) 3x ou mais no cartão: 20% de juros                -=- \n')
print(' -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ')
print(' ')
cdp = int(input('DIGITE A OPÇÃO CORRESPONDENTE O MENU ACIMA: '))
print('PROCESSANDO...')
sleep(2)
# Condições de pagamento de acordo com o input do usuario
print(' ')
if cdp == 1:
    vdp = vdp - (vdp * 10 / 100)
    print('Valor do produto é: R$ {:.2f} \nA vista com 10% de desconto é: R$ {:.2f}'.format(vsd, vdp))
elif cdp == 2:
    vdp = vdp - (vdp * 5 / 100)
    print('Valor do produto é: R$ {:.2f} \nA vista com 5% de desconto é: R$ {:.2f}'.format(vsd, vdp))
elif cdp == 3:
    print('Valor do produto é: R$ {:.2f} \nem até 2x permanece o valor original de: R$ {:.2f}'.format(vdp, vdp))
elif cdp == 4:
    parcelas = int(input('Quantas vezes no cartão: '))
    vdp = vdp + (vdp * 20 / 100)
    xnc = vdp / parcelas
    print('Valor do produto é: R$ {:.2f} \n{}x no cartão o valor do produto e acrescido em 20% de juros, resultando em um total de: R$ {:.2f} e cada parcela fica no valor de: R$ {:.2f}'.format(vsd, parcelas, vdp, xnc))
else:
    print('Erro, opção invalida tente novamente!.')
print(' ')
