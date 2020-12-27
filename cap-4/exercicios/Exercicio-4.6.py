# Exercicio 4.6 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 Km, e R$ para viagens mais longas
print ('    ')
dist = int(input('Informe a distancia do trajeto: '))
distm = 0.50
distma = 0.20
# Condição e calculo
print ('    ')
if dist <= 200:
    tppd = dist * distm
else:
    tppd = dist * distma
print (f'O valor total a ser pago pela viagem é: R${tppd:5.2f}, Obrigado por viajar conosco!')
print ('    ')
