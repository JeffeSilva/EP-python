#!/ust/bin/env python
sexo = str(input('Informe o sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informe um dado valido: [M/F] ')).strip().upper()[0]
print('Sexo cadastrado com sucesso!')
print('Fim ')