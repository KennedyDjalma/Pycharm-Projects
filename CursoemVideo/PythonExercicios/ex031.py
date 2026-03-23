'''
DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM
EM KM. CALCULE O PREÇO DA PASSAGEM, COBRANDO 0,50 POR KM PARA
VIAGENS DE ATÉ 200KM E 0,45 PARA VIAGENS MAIS LONGAS
'''


distancia = float(input('qual o total da distancia? '))
print('voce vai viajar {} kms'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('o preço da passagem será {:.2f}'.format(preco))
