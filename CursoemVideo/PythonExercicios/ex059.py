'''
  -------------------------------------------------
    59-
    CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE
    UM MENU NA TELA:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA
    SEU PROGRAMA DEVERA REALIZAR A OPERAÇÃO SOLICITADA
    EM CADA CASO.
    ------------------------------------------------
'''
from time import sleep
print('=-='*10)

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA
    ''')
    opcao = int(input('>>>>>>>>Qual a sua opção?<<<<<< '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))

    elif opcao == 2:
        produto = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, produto))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))

    elif opcao == 4:
        print('informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('opcao invalida')
    print('=-='*10)
    sleep(4)

print('Fim do programa! ')


