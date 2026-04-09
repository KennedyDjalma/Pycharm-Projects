'''
CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE
PESSOAS. NO FINAL MOSTRE QUANTAS SÃO MAIORES DE IDADES
E QUANTAS NÃO SÃO.
'''
from datetime import date
atual = date.today().year

for pessoa in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = atual - nascimento
    print('Essa pessoa tem {} anos'.format(idade))

    if idade >= 18:
        print('Essa pessoa é \033[0;34mMAIOR.\033[m')
    else:
        print('Essa pessoa é \033[0;31mMENOR.\033[m')
print('\033[4;35mFIM DO PROGRAMA')
