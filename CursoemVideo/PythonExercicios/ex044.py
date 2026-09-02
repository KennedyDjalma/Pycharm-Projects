'''
ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM
PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
- A VISTA DINHEIRO / CHEQUE
- A VISTA NO CARTÃO: 5% DESCONTO
- EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
- 3X OU MAIS NO CARTÃO: 20% DE JUROS
'''

print('\033[1;34m LOJA DESCONTÃO SEM CARTÃO \033[0m')

preco = float(input('Digite o valor dos produtos: R$'))
print('''\033[1;32m FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x: preço normal
[ 4 ] 3x no cartão: 20% de juros \033[0m''')

opcao = int(input('\033[0;33m Qual é a forma de pagamento? \033[0m'))
if opcao == 1:
   total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('\033[1;35m Sua compra sera parcelada em até 2x de R${:.2f}\033[0m'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparcela  = int(input('Quantas parcelas? '))
    parcela = total / totalparcela
    print('\033[0;34m Sua compra será parcelada em {}x de R${:.2f}\033[0m'.format(totalparcela, parcela))
else:
    total = preco
    print('\033[4;31m OPÇÃO INVALIDA!!! VERIFIQUE NOVAMENTE \033[0m')
print('\033[1;35m Sua compra de R${} ficou por {} \033[0m'.format(preco, total))
