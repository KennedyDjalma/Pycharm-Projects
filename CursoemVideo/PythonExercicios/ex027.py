'''
FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA.
MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME
SEPARADAMENTE.
EX: Kennedy Djalma de Santana
PRIMEIRO = Kennedy
ULTIMO = Santana
========================================================

nome = nome.split()     =   vai pegar o nome completo
e vai ler separadamente.

.format(nome[len(nome)-1])  = ele mede o comprimento do
nome informado e vai pegar o ultimo nome.
'''

nome = str(input('digite seu nome completo: ')).strip()
nome = nome.split()
print('Muito prazer em te conhecer {}'.format(nome [0]))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))

