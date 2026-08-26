'''pessoas = [['Pedro', 25], ['Maria', 19], ['joão', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])'''

''' EXEMPLO 1
teste = list()
teste.append('Kennedy')
teste.append(30)

galera = list()
galera.append(teste[:])

teste[0] = 'Djalminha'
teste[1] = 19
galera.append(teste[:])

print(galera)
'''

''' EXEMPLO 2
galera = [['joao', 34], ['ana', 22], ['bia', 25], ['rita', 28]]
print(galera [3])
'''

''' EXEMPLO 3
galera = [['joao', 34], ['ana', 22], ['bia', 25], ['rita', 28]]
for pessoa in galera:
    print(pessoa[0])
'''

''' EXEMPLO 4
galera = [['joao', 34], ['ana', 22], ['bia', 25], ['rita', 28]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]}  de idade.')
'''

galera = list()
dado = list()
totmai = totmen = 0
for contador in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmen +=1
        print(f'Temos {totmai} maioress e {totmen} menores de idade.')

''' EXERCICIO 84
FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VARIAS PESSOAS,
GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:
A - QUANTAS PESSOAS FORAM CADASTRADAS.
B - UMA LISTAGEM COM AS PESSOAS MAIS PESADAS.
C - UMA LISTAGEM COM AS PESSOAS MAIS LEVES.
'''

''' EXERCICIO 85
CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR SETE
VALORES NUMERICOS E CADASTRE-OS EM UMA LISTA UNICA 
QUE MANTENHA SEPARADOS OS VALORES PARES E IMPARES.
NO FINAL, MOSTRE OS VALORES PARES E IMPARES EM ORDEM
CRESCENTE.
'''

''' EXERECICIO 86
CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSAO 3X3
E PREENCHA COM VALORES LIDO PELO TECLADO.
NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMAÇAÕ CORRETA.
'''

''' EXERCICIO 87
APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:
A - A SOMA DE TODOS OS VALORES PARES DIGITADOS.
B - A SOMA DOS VALORES DA TERCEIRA COLUNA.
C - O MAIOR VALOR DA SEGUNDA LINHA.
'''

''' EXERCICIO 88
FACA UM PROGRAMA  QUE AJUDE UM JOGADOR DA MEGA SENA A 
CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS
SERAO GERADOS E VAI SORTEAR 6 NUMEROS ENTRE 1 E 60 PARA
CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA.
'''

''' EXERCICIO 89
CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VARIOS
ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA. NO FINAL,
MOSTRE UM BOLETIM CONTENDO A MEDIA DE CADA UM E PERMITA
QUE  OS USUARIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO
INDIVIDUALMENTE.
'''