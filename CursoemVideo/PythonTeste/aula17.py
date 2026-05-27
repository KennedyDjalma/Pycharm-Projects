'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(4) # acrescenta o numero no final
num.sort() # organiza os numeros
num.reverse() # organiza de traz para frente
num.insert(2, 0) # acrescenta na posição 2 o numero 0
num.pop(2) # remove o numero da posição 2

# procura o numero 9 na lista e remove ele da poisção que estiver
if 9 in num:
    num.remove(9)
else:
    print('NÃO ACHEI O NUMERO para remover')

print(num)
print(f'essa lista tem {len(num)} elementos') # mostra tamanho dos elementos
'''

'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}... ', end='')
'''

'''
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
'''

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}')
print('Cheguei ao final da lista')

'''
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
78
FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMERICOS E GUARDE-OS
EM UMA LISTA.
NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO
E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
79
CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR VARIOS
VALORES NUMERICOS E CADASTRE-OS EM UMA LISTA. CASO O 
NUMERO JA EXISTA LA DENTRO, ELE NÃO SERA ADICIONADO.
NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES UNICOS
DIGITADOS, EM ORDEM CRESCENTE.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
80
CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR CINCO
VALORES NUMERICOS E CADASTRE-OS EM UMA LISTA, JA NA
POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SIRT()).
NO FINAL, MOSTRE A LISTA ORDENADA NA TELA.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
81
CRIE UM PROGRAMA QUE VAI LER VARIOS NUMEROS E COLOCAR
EM UMA LISTA. DEPOIS DISSO, MOSTRE:
A - QUANTOS NUMEROS FORAM DIGITADOS.
B - A LISTA DE VALORES, QORDENADA DE FORMA DECRESCENTE.
C - SE O VALOR 5 FOI DIGITADO E ESTA OU NAO NA LISTA.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
82
CRIE UM PROGRAMA QUE VAI LER VARIOS NUMEROS
E COLOCAR UMA LISTA. DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS
QUE VÃO CONTER APENAS OS VALORES PARES E OS VALORES IMPARES
DIGITADOS, RESPECTIVAMENTE. NO FINAL, MOSTRE O CONTEUDO
DAS TRES LISTAS GERADAS.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
83
CRIE UM PROGRAMA ONDE O USUARIO DIGITE UMA EXPRESSÃO
QUALQUER QUE USE PARENTESES. SEU APLICATIVO DEVERÁ 
ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARENTESES
ABERTOS E FECHADOS NA ORDEM CORRETA.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
'''
