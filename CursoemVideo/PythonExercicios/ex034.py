'''
ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DO FUNCIONARIO
E CALCULE O VALOR DO SEU AUMENTO. PARA SALARIO SUPERIOR A
1250,00, CALCULE UM AUMENTO DE 10%.
PARA INFERIORES OU IGUAIS, O AUMENTO É DE 155
'''

salario = float(input('Salario: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
    print('Salario antigo é de {}, e o novo {}'.format(salario, novo))