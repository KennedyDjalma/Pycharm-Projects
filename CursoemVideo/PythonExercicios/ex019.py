'''
UM PROFESSOR QUER SORTEAR UM DOS SEUS ALUNOS PARA APAGAR O
QUADRO. FAÇA UN PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES
E ESCREVENDO O NOME DO ESCOLHIDO.
'''
'''
import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome; ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))
'''

from random import choice
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome; ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))
