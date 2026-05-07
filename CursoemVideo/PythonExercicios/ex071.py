'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
71
CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM
CAIXA ELETRONICO. NO INICIO, PERGUNTE AO USUARIO
QUAL O VALOR SACADO (VALOR INTEIRO) E O PROGRAMA
VAI INFORMAR QUANTAS CEDULAS DE CADA VALOR SERÃO
ENTREGUES. OBS: CONSIDERE QUE O CAIXA POSSUI
CEDULAS DE R$50, R$20, R$10, E R$1.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''

print('\033[0;34m=-\033[0m' *20)
print('{:^30}'.format('BANCO KENNEDY'))
print('\033[036m-=\033[0m' *20)
valor = int(input('Qual o valor do saque: R$'))
total = valor
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print('Total de {} cedulas de R${:.2f}'.format(totcedula, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('\033[0;34m=-\033[0m' *20)





