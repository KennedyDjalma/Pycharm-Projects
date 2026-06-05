'''
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
82
CRIE UM PROGRAMA QUE VAI LER VARIOS NUMEROS
E COLOCAR UMA LISTA. DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS
QUE VÃO CONTER APENAS OS VALORES PARES E OS VALORES IMPARES
DIGITADOS, RESPECTIVAMENTE. NO FINAL, MOSTRE O CONTEUDO
DAS TRES LISTAS GERADAS.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
'''

num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
for indice, valor in enumerate(num):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print('-' * 40)
print(f'LISTA COMPLETA {num}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')
