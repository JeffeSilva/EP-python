#!/usr/bin/env python
# Variaveis globais
mes = 1
# Entrada do usuario
divida = float(input('Informe o valor da divida: '))
juros = float(input('Informe o juros mensal: '))
pagamento = float(input('Informe o valor pago por mês: '))
# Logica
if divida * (juros / 100) > pagamento:
    print('O juros da divida é maior que o valor de pagamento.')
else:
    saldo = divida
    jurospg = 0
    while saldo > pagamento:
        juros = saldo * (juros / 100)
        saldo = saldo + juros - pagamento
        jurospg += juros
        print(f'O valor da divida pago no mes {mes} e de R$ {saldo:.2f}')
        mes += 1
    print(f'Para pagar uma divida de R$ {divida:6.2f}, a {juros:5.2f} % de juros')
    print(f'Você precisara de {mes} meses, pagamento um total de R$ {jurospg:5.2f}')
    print(f'No ultimo mês, você teria um saldo residual de R$ {saldo:6.2f} a pagar.')