'''
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
81
CRIE UM PROGRAMA QUE VAI LER VARIOS NUMEROS E COLOCAR
EM UMA LISTA. DEPOIS DISSO, MOSTRE:
A - QUANTOS NUMEROS FORAM DIGITADOS.
B - A LISTA DE VALORES, QORDENADA DE FORMA DECRESCENTE.
C - SE O VALOR 5 FOI DIGITADO E ESTA OU NAO NA LISTA.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
'''

# A - QUANTOS NUMEROS FORAM DIGITADOS.
valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-=' * 20)
print(f'Voce digitou {len(valores)} elementos')
# B - A LISTA DE VALORES, QORDENADA DE FORMA DECRESCENTE.
valores.sort(reverse=True)
print(f'Voce digitou os valores {valores}')
# C - SE O VALOR 5 FOI DIGITADO E ESTA OU NAO NA LISTA.
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não esta na lista')
