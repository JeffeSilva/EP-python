# Programa 4.3 - Cálculo do Imposto de renda
print ('    ')
salario = float(input('Digite o salário para cálculo do imposto: '))
base = salario
imposto = 0
# Estrutura das condições
print ('    ')
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print (f'Salario: R${salario:6.2f} Imposto a pagar: R${imposto:6.2f}')
print ('    ')
