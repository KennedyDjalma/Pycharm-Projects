'''
-------------------------------------------------
62-
MELHORE O DESAFIO 61, PERGUNTANDO PARA O USUARIO
SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA
ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR
'0 TERMOS'
------------------------------------------------
'''

print('Gerador de PA')
print(' - =' * 10)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 1
total = 0
mais = 10
while contador != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input(' quanto termo voce quer mostrar Mais? '))
print('Progressão finalizada com {} termos'.format(total))
