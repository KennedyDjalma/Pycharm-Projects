'''
ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM VEICULO.
SE ELA ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO:
A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE
'''

km = float(input('Qual a velocidade do carro? '))
if km > 80:
    print('A multa vai custar R$7,00 por km acima da velocidade')
    multa = (km -  80) * 7
    print('voce vai pagar a multa de R${:.2f}!'.format(multa))
else:
    print('Voce dirige bem! sua velocidade atual é: {}km/h'.format(km))