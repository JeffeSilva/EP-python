print('')
print('=' * 21)
print(' BANCO EXERCICIO 071 ')
print('=' * 21)
print('')
num = int(input('Qual valor deseja sacar: '))
dinheiro = num
#Número de notas
notas = 50
totalnotas = 0
#Logica das notas
while True:
    if dinheiro >= notas:
        dinheiro -= notas
        totalnotas += 1
    else:
        print(f'O total de {totalnotas} notas de R${notas}')
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        totalnotas = 0
        if dinheiro == 0:
            break
