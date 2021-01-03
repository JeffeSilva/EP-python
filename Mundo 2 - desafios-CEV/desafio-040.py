#!/usr/bin/env python
# entrada de informações
nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
# condições de acordo com a média
if media <= 4.9:
    print('O aluno {} obteve a média {} e foi reprovado!'.format(nome, media))
elif media <= 6.9:
    print('O aluno {} obteve a média {} e encontra-se me recuperação!'.format(nome, media))
elif media >= 7:
    print('O aluno {} obeteve a média {} e foi aprovado com louvor!'.format(nome, media))
else:
    print('Dados invalidos, verifique e tente novamente!')