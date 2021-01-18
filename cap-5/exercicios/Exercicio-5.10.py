#!/usr/bin/env python
nome = str(input('Digite seu nome: '))
p = 0
gues = 1
while gues <= 3:
    resposta = input(f'Resposta da questão {gues}°: ').lower()
    if gues == 1 and resposta == 'b':
        p += 1
    if gues == 2 and resposta == 'a':
        p += 1
    if gues == 3 and resposta == 'd':
        p += 1
    gues += 1
print(f'O aluno {nome} fez {p} pontos(s).')