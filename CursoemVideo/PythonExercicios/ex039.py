'''
FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E
INFORME DE ACORDO COM SUA IDADE, SE ELE AINDA VAI SE ALISTAR AO
SERVIÇO MILITAR, SE É A HORA DE SE ALISTAR OU SE JA PASSOU DO
TEMPO DO ALISTAMENTO.
SEU PROGRAMA TAMBEM DEVERA MOSTRAR O TEMPO QUE FALTA OU QUE
PASSOU DO PRAZO.
'''

from datetime import date #serve para importar a classe date do módulo datetime,
# que é usada para trabalhar com datas (dia, mês e ano) de
# forma simples.
atual = date.today().year # pega o ano atual
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar \033[0;31m imediatamente')
elif idade < 18:
   # #saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(idade-18))
elif idade > 18:
    #saldo = 18 - idade
    print('Voce deveria ter se alistado há {} anos'.format(idade-18))
