'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
75
DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO
TECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:
A - QUANTAS VEZES APARECEU O VALOR 9.
B - EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3.
C - QUAIS FORAM OS NUMEROS PARES.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

num = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')))

print(f'Você digitou os números {num}')

#A - QUANTAS VEZES APARECEU O VALOR 9.
print(f'O valor 9 apareceu {num.count(9)} vezes')

#B - EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3.
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O numero 3 não foi digitado.')

#C - QUAIS FORAM OS NUMEROS PARES.
print(f'Os valores digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')
