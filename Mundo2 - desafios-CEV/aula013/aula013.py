from time import sleep
n = int(input('Informe um número: '))
for c in range(n, 0, -1):
    print(c), sleep(1)
print('Fim')