'''
A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA
QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA
DE ACORDO COM A IDADE:
-ATÉ 9 ANOS: MIRIM
-ATÉ 14 ANOS: INFANTIL
-ATÉ 19 ANOS: JUNIOR
-ATÉ 25 ANOS: MASTER
'''

from datetime import date

atual = date.today().year

ano = int(input('Ano de nascimento: '))
idade = atual - ano
if idade <= 9:
    print('\033[0;32m Atleta {} Anos MIRIM'.format(idade))
elif idade <= 14:
    print('\033[0;33m Atleta {} Anos INFANTIL'.format(idade))
elif idade <= 19:
        print(' \033[0;34m Atleta {} Anos JUNIOR'.format(idade))
elif idade <= 25:
    print('\033[0;35m Atleta {} Anos MASTER'.format(idade))
