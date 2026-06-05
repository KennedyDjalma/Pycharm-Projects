'''
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
83
CRIE UM PROGRAMA ONDE O USUARIO DIGITE UMA EXPRESSÃO
QUALQUER QUE USE PARENTESES. SEU APLICATIVO DEVERÁ
ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARENTESES
ABERTOS E FECHADOS NA ORDEM CORRETA.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
'''

expressao = str(input('digite a expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop() #.pop remove o ultimo elemento da lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta errada!')

    