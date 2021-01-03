#!/usr/bin/env python
#USUARIO ENTRA COM AS INFORMAÇÕES
print(' ')
imo = float(input('Informe o valor do imóvel: '))
sal = float(input('Informe o seu salário: '))
ano = int(input('Em quanto tempo deseja pagar: '))
#CALCULOS DE 30% E PERIODO DE PAGAMENTO
par = imo / (ano * 12)
tpds = (sal * 30) / 100
#PROGRAMA TESTANDO CLIENTE
print(' ')
if par > tpds:
    print('O valor da parcela é R$ {:.2f}, é o seu salário é R$ {:.2f} infelizmente excede o limite de 30% do seu salário que é {:.2f}o Sr(a). não é apto para adquirir este financiamento.'.format(par, sal, tpds))
else:
    print('O valor da parcela é R$ {:.2f}, seu salário é {:.2f}, e o prazo total de pagamento é:'.format(par, sal),(ano * 12),'meses!')
print(' ')
