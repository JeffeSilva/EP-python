#usr/bin/env python
print(' ')
vel = float(input('Informe a velocidade do veiculo: '))
if vel > 80:
    preco = (vel - 80) * 7
    print(f'Você deve pagar uma multa de R$ {preco:.2f}, por excesso de velocidade!')
else:
    print('Parabéns você é um motorista exemplar!')
print(' ')