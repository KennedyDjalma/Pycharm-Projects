'''
DESENVOLVA UM PROGRAMA QUE LEIA O PESO E A ALTURA DE UMA PESSOA,
CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
- ABAIXO DE 18.5: ABAIXO DO PESO
- ENTRE 18.5 E 25: PESO IDEAL
- ENTRE 25 E 30: SOBREPESO
- ENTRE 30 E 40: OBESIDADE
- ACIMA DE 40: OBESIDADE MÓRBIDA
'''

peso = float(input('Qual o seu peso: (Kg) '))
altura = float(input('Qual a sua altura: (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[1;31m Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('\033[1:32m Peso ideal')
elif imc >= 25 and imc <= 30:
    print('\033[2;33m Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('\033[3;33m Obesidade')
else:
    print('\033[4;34m Obesidade Morbida')
