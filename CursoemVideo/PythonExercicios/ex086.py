''' EXERECICIO 86
CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSAO 3X3
E PREENCHA COM VALORES LIDO PELO TECLADO.
NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMAÇAÕ CORRETA.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha] [coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))

print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^11}]', end='') #:^11  FORMATAÇÃO DE ESPAÇOS
    print()