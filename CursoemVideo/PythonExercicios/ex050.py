'''
DESENVOLVA UM PROGRAMA QUE LEIA 6 NUMEROS INTEIRO E
MOSTRE A SOMA DOS PARES. SE FOR DIGITADO IMPAR, DESCONSIDERE
'''


soma = 0
contador = 0
for c in range(1, 7):
    num = int(input(' Digite um valor: '))
    if num % 2 == 0:
        soma += num
        contador += 1
print('Voce informou e a soma foi {}'.format(soma))
