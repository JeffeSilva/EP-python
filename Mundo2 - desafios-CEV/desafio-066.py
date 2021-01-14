#!/usar/bin/env python
c = 0
soma = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    soma += num
    c += 1
print(f'Foram digitados {c} números e a soma de todos eles é {soma}.')