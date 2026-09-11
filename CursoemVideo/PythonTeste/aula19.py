# tuplas ()
# listas []
# dicionarios {}

''' ex01
dados = dict()
dados = {'nome':'pedro', 'idade':25}
print(dados)
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M' # acrescentar mais um dado no dicionario
print(dados['sexo'])
del dados['idade'] # deleta um dado do dicionario
'''

''' ex02
filme = {'Titulo':'Star wars',
         'Ano':1977,
         'Diretor':'George L.'}
print(filme.values()) # Star wars', 1977, 'Jorge L.
print(filme.keys()) # Titulo', 'Ano', 'Diretor
print(filme.items()) # ('Titulo', 'Star wars'), ('Ano', 1977), ('Diretor', 'Jorge L.')

# para usar nos laços
for k, v in filme.items():
    print(f'O {k} é {v}') # k = chave, v = valor
'''

''' ex03
# declarando dicionario
pessoas = {'Nome': 'knd', 'Sexo': 'M', 'Idade': 24}
print(pessoas)

#pessoas['Nome'] = 'Kenned' #troca o nome do dicionario

print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')  # O knd tem 24 anos.
print(pessoas.values())  # dict_values(['knd', 'M', 24])
print(pessoas.keys())  # dict_keys(['Nome', 'Sexo', 'Idade'])
print(pessoas.items())  # dict_items([('Nome', 'knd'), ('Sexo', 'M'), ('Idade', 24)])

for k in pessoas.values():
    print(k)
'''

''' ex04
brasil = [] #criando a lista com dicionarios

estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF' : 'Sao Paulo', 'Sigla': 'SP'}

#adicionando elemento na lista
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1] ['UF']) #Sao Paulo
'''

''' ex05
estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #copy() serve para copiar como usar o :  .
#print(brasil)

for e in brasil:
    print(e)
'''
# DESAFIOS

'''
EX090
FAÇA UM PROGRAMA QUE LEIA NOME E A MEDIA DE UM ALUNO,
GUARDANDO TAMBEM A SITUAÇÃO EN UM DICIONARIO.
NO FINAL, MOSTRE O CONTEUDO DA ESTRUTURA NA TELA.
'''

'''
EX091
CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUE UM DADO E TENHA 
RESULTADOS ALEATORIOS. GUARDE ESSES RESULTADO EM UM
DICIONARIO. NO FINAL, COLOQUE ESSE DICIONARIO EM ORDEM,
SABENDO QUE O VENCEDOR TIROU MAIOR NUMERO NO DADO.
'''

'''
EX092
CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO 
E CARTEIRA DE TRABALHO E CADASTRE-OS (COM IDADE)
EM UM DICIONARIO SE POR ACASO  A CTPS FOR DIFERENTE
DE ZERO, O DICIONARIO RECEBERA TAMBEM O ANO DE
CONTRATAÇÃO E I SAKARUI. CALCULE E ACRESCENTE, ALEM
DA IDADE,COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR.
 '''

'''
EX093
CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM
JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR
E QUANTAS PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE
DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TIDP ISSO SERA
GUARDADO EM UM DICIONARIO, INCLUINDO O TOTAL DE GOLS
FEITOS DURANTE O CAMPEONATO.
'''

'''
EX094
CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VARIAS
PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONARIO
E TODOS OS DICIONARIOS EM UMA LISTA. NO FINAL, MOSTRE:
A - QUANTAS PESSOAS FORAM CADASTRADAS.
B - A MEDIA DE IDADE DO GRUPO.
C - UMA LISTA COM TODAS AS MULHERES.
D - UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MEDIA.
'''

'''
EX095
APRIMORE O DESAFIO 093 PARA QUE ELE FUNCIONE COM VARIOS
JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE 
DETALHES DO APROVEITAMENTO DE CADA JOGADOR.
'''
