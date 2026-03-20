'''
DIVIDINDO OS DIGITOS DE UM NUMERO.
FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE
NA TELA CADA UM DOS DIGITOS SEPARADOS.
EX: DIGITE UM NUMERO: 1234
UNIDADE:4. DEZENA3. CENTENA:8. MILHAR:1.
'''


num = int(input('Informe um numero: '))
u = num // 1 % 10 # usando o %10 ele pega o ultimo digito
d = num // 10 % 10 #  se usar %100 ele vai pegar 2 digitos
c = num // 100 % 10 # se usar %1000 ele vai pegar 3 digitos
m = num // 1000 % 10 #se usar %10000 ele vai pegar 4 digitos
print('Analizando o numero {}'.format(num))
print   ('Unidade: {}' .format(u))
print   ('Dezena: {}'  .format(d))
print   ('Centena: {}' .format(c))
print   ('Milhar: {}'  .format(m))








