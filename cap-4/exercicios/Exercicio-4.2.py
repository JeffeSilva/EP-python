# Exercicio 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 Km/h.
print('    ')
vldc = int(input('Informe a velocidade do Veiculo: '))
lvpm = 80
print('    ')
# Condição e formula
if vldc <= lvpm:
    print ('Você e um cidadão responsavel, e não deve ser multado')
if vldc > lvpm:
    vdm = (vldc - lvpm) * 5
    if vdm > 0:
        print (f'Você foi multado por excesso de velocidade, {vldc:3.1f}Km/h o valor da multa é R${vdm:5.2f}')
print('    ')

