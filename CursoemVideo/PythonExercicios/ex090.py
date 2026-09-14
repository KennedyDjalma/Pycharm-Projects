'''
EX090
FAÇA UM PROGRAMA QUE LEIA NOME E A MEDIA DE UM ALUNO,
GUARDANDO TAMBEM A SITUAÇÃO EN UM DICIONARIO.
NO FINAL, MOSTRE O CONTEUDO DA ESTRUTURA NA TELA.
'''

# criando o dicionario
aluno = dict()

aluno['nome'] = str(input('Nome: '))  # O usuario vai digitar o nome
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))  # O usuario vai digitar a media

if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUMPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'

print('-=' *30)

for k, v in aluno.items():
    print(f'    - {k} é igual a  {v}')

print('-=' *30)