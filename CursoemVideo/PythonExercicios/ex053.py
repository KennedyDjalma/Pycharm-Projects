'''
CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA
SE ELA É UM PALINDROMO, DESCONSIDERANDO OS ESPAÇOS.
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    print(junto[letra])
    inverso += junto[letra]

if inverso == junto:
    print('Palindromo')
else:
    print('NÂO é Palindromo')
