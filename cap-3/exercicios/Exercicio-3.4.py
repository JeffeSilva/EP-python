# Exercicio 3.4 - Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário pe maior que R$ 1.200,00.
# Interação Usuario e Variavel de teste
print ('---------------- Inicio do Programa ---------------')
print ('    ')
sal = float(input('Informe o seu salário: '))
imp = float (1200.00)
#Expressão para saber se paga ou não imposto
poni = sal > imp
print (f'Se o resultado e True - Paga Imposto')
print (f'Se o resultado for False - Não paga Imposto')
print (f'O resultado é {poni}.')
print ('    ')
print ('----------------- Fim do Programa -----------------')
