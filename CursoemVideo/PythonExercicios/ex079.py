'''
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
79
CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR VARIOS
VALORES NUMERICOS E CADASTRE-OS EM UMA LISTA. CASO O
NUMERO JA EXISTA LA DENTRO, ELE NÃO SERA ADICIONADO.
NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES UNICOS
DIGITADOS, EM ORDEM CRESCENTE.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
'''

numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')

    else:
        print('Valor duplicado. Digite novamente.')
    # RESPOSTA INPUT
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'N':
        break

numeros.sort() #OS NUMEROS EM ORDEM CRESCENTE
print(f'voce digitou os valores: {numeros}')
