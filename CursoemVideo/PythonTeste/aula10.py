'''
nome = str(input('Seu nome: '))
if nome == 'Kennedy':
    print('Olá Senhor {}'.format(nome))
else:
    print('Seu nome é normal.')
print('Bom dia {}'.format(nome))
'''

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(media))
if media >= 6.0:
    print('Sua nota foi boa')
else:
    print('Sua nota foi ruim')