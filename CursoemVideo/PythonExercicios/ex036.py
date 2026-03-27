'''
ESCREVA UM PROGRAMA PARA APROVAR O EMPRESTIMO BANCARIO PARA A
COMPRA DE UMA CASA. PERGUNTE O VALOR DA CASA, O SALARIO DO
COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
A PRESTAÇÃO MENSAL NAO PODE EXECER 30% DO SALARIO OU ENTÃO
O EMPRESTIMO É NEGADO
'''

casa = float(input('Valor da casa: R$'))
salario = float(input('Salario: R$'))
anos = int(input('Quantos anos deseja pagar: '))
prestacao = casa / (anos * 12)
minimo= salario * 30 / 100

print('Para pagar a casa de R${:.2f} em {} anos.'.format(casa, anos, end=''))
#end=''   SERVE PARA NAO TER QUEBRA DE LINHA DE UM PRINT PARA O OUTRO
print('A prestação será de {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('\033[34m Emprestimo CONCEDIDO')
else:
    print('\033[31m Emprestimo NEGADO')
