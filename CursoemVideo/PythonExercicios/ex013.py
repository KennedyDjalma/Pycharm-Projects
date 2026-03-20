# FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONARIO
#E MOSTRE SEU NOVO SALARIO, COM 15% DE AUMETO.

salario = float(input('Qual é o salario? R$'))
novo = salario + (salario * 15 / 100)
print('O funcionario que ganhava R${:.2f}, com 15% a mais, \n passa a receber R${:.2f}'.format(salario, novo))
