'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
72
CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA
COM UMA CONTAGEM POR EXTENSO, DEZERO ATÉ VINTE.
SEU PROGRAMA DEVERÁ LER UM NUMERO PELO TECLADO
ENTRE (0 E 20) E MOSTRA-LO POR EXTENSO.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove',
        'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end=' ')

print(f'Voce digitou o número {cont[num]}')
