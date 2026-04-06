'''
FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRECIVA
PARA O ESTOURO DE FOGOS DE ARTIFICIO, INDO DE 10 ATÉ 0,
COM PAUSA DE 1 SEGUNDO ENTRE ELES.
'''
from time import sleep

print('CONTAGEM REGRESSIVA')
for c in range(10,0 -1, -1):
    sleep(0.3)
    print (c)
    sleep(0.5)
print('\033[4;36mOLÁ MUNDO')

