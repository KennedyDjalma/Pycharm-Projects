# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE
# SEU NOVO PREÇO, COM 5% DE DESCONTO.

preço = float(input('Qual o Preço? R$'))
novo = preço - (preço * 5 / 100)
print('O preço era {:.2f}, com o desconto é {:.2f}'.format(preço, novo))
