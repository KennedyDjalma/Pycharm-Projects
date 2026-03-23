'''
FAÇA UM PROGRAMA QUE LEIA TRES NUMEROS E MOSTRE QUAL
 É O MAIOR E O MENOR
'''

a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('o menor valor digitado foi {}'.format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o maior valor digitado foi {}'.format(maior))
