'''
ESCREVA UM PROGRAMA QUE LEIA DOIS NUMERO INTEIROS E COMPARE-OS
MOSTRANDO NA TELA UMA MENSAGEM;
- O PRIMEIRO VALOR É MAIOR
- O SEGUNDO VALOR É MAIOR
- NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS
'''

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O primeiro numero é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Os valores são iguais')
