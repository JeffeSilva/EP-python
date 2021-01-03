#!/usr/bin/env python
#Entrada dos dados pelo ususario, Peso e Altura
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura ** 2)
#Regras e Condições
if imc < 18.5:
    print('Você esta com IMC de {:.2f} abaixo do peso!'.format(imc))
elif imc < 25:
    print('Você esta com IMC de {:.2f} no peso ideal!'.format(imc))
elif imc < 30:
    print('Você esta com IMC de {:.2f} sobre peso, Atenção!'.format(imc))
elif imc < 40:
    print('Você esta com IMC de {:.2f} obeso procure um medico!'.format(imc))
elif imc > 40:
    print('Você esta com IMC de {:.2f} obesidade morbida e deve ter um acompanhamento especializado!'.format(imc))