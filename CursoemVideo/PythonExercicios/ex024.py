'''
CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE
ELA COMEÇA OU NAO COM O NOME 'SANTO'.
.strip()   REMOVE OS ESPAÇOS ANTES DO NOME
.upper()   O QUE DIGITAR VAI FICAR EM MAIUSCULO E JULGAR SE É 1 || -1
'''

cidade = str(input('Digite o nome de sua cidade: ')).strip()
print(cidade[0:5].upper() == 'SANTO')
