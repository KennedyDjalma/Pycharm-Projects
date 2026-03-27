'''
ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E PEÇA
PARA O USUARIO ESCOLHER QUAL SERÁ A BASE DE CONVERSAO:
- 1 PARA BINARIO
- 2 PARA OCTAL
- 3 PARA HEXADECIMAL
'''

num = int(input('\033[36m Digite um numero inteiro: \033[0m'))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para Binario
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('\033[0;35m {} convertido para binario é igual a {}'.format(num, bin(num)[2:])) #[2:] é a fatiamento de string
elif opcao == 2:
    print('\033[0;33m {} convertido para octal é igual a {}'.format(num, oct(num)[2:])) #[2:] é a fatiamento de string
elif opcao == 3:
    print('\033[0;32m {} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:])) #[2:] é a fatiamento de string
else:
    print('\033[31m Opção invalida!')