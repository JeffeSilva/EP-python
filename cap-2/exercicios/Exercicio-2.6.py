# Exercicio 2.6 - Modifique o Programa 2.2, de forma que ele calcule um aumento de 15% para um salário de R$ 750.
sal = 750
aum = 15
# formula e variavel recebendo resultado
salcaum = sal + (sal * aum / 100)
# Mostrando valores formatados.
print(f'Salario R$ {sal:5.2f} recebeu um aumento de {aum}% o total é {salcaum:5.2f}')
