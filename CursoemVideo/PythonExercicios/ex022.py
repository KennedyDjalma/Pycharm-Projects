'''
CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA
E MOSTRE:
-O NOME COM TODAS AS LETRAS MAIUSCULAS E MINUSCULAS.
-QUANTAS LETRAS AO TODO (SEM CONSIDERAR OS ESPAÇOS).
-QUANTAS ÇETRAS TEM O PRIMEIRO NOME.
'''

nome = str(input('Digite seu nome completo: ')).strip()
# .strip() = vai eliminar os espaços antes e depois do nome

print ('Analisando seu nome...')

# LETRAS MAIUSCULAS
print ('Seu nome em maiusculas é {}'.format(nome.upper()))

# LETRAS MINUSCULAS
print ('Seu nome em minusculas é {}'.format(nome.lower()))

# TOTAL DE LETRAS NO NOME. Usando: .format(len(nome)-nome.count(' ')))
# VAI ELIMINAR OS ESPAÇOS ENTRE OS NOMES
print ('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))

# USANDO O: (nome.find(' ')) ELE VAI INFORMAR O TAMANHO DO PRIMEIRO NOME
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

# SE USAR O: nome.split() .ELE VAI VER O NOME QUE FOI PEDIDO E
# INFORMAR A QUANTIDADE DE LETRAS QUE TEM NO NOME USANDO:
# .format(separa[0], len(separa[0])))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

