'''
EX092
CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO
E CARTEIRA DE TRABALHO E CADASTRE-OS (COM IDADE)
EM UM DICIONARIO SE POR ACASO  A CTPS FOR DIFERENTE
DE ZERO, O DICIONARIO RECEBERA TAMBEM O ANO DE
CONTRATAÇÃO E I SAKARUI. CALCULE E ACRESCENTE, ALEM
DA IDADE,COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR.
'''

from datetime import datetime

dados = dict()
dados['Nome'] = str(input('NOME: '))
nascimento = int(input('ANO DE NASCIMENTO: '))
dados['idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('CTPS: '))

if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35 - datetime.now().year)
print(dados)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
