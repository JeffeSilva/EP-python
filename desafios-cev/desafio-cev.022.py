#!/usr/bin/env python
# Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras minusculas, o nome com todas as letras maiusculas, quantas letras tem sem considerar espaços, e quantas letras tem o primeiro nome.
print (' ')
nome = str(input('Digite seu nome completo: '))
print('O seu nome em minusculas:',nome.lower())
print('O seu nome em maiusculas:',nome.upper())
nl = nome.split()
ldpn = len(nl[0])
njl = ''.join(nl)
print(f'O seu nome sem considerar os espaços tem:',len(njl),'caracteres, é o seu primeiro nome tem',len(nl[0]),'caracteres.')
print(' ')
