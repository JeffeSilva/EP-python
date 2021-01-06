#!/usr/bin/env python
# entrada de informações
nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
# condições de acordo com a média
if media <= 4.9:
    print('O aluno {} tirou as notas {:.1f} e {:.1f}, e obteve a média {:.1f} e foi reprovado!'.format(nome, nota1, nota2, media))
elif media <= 6.9:
    print('O aluno {} tirou as notas {:.1f} e {:.1f}, obteve a média {:.1f} e encontra-se em recuperação!'.format(nome, nota1, nota2, media))
elif media >= 7:
    print('O aluno {} tirou as notas {:.1f} e {:.1f}, obeteve a média {:.1f} e foi aprovado com louvor!'.format(nome, nota1, nota2, media))
else:
    print('Dados invalidos, verifique e tente novamente!')
