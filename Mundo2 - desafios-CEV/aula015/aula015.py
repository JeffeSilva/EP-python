num = 0
soma = 0
while True:
    num = int(input('Informe um número: '))
    if num == 999:
        break #O break joga IMEDIATAMENTE PARA FORA DO LAÇO
    soma += num
print(f'A soma dos números digitados é {soma}') # QUANDO BREAK E VERDADEIRO É EXECUTADO DIRETAMENTE FORA DO LAÇO.
print('FIM ')
