''' EXERCICIO 84
FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VARIAS PESSOAS,
GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:
A - QUANTAS PESSOAS FORAM CADASTRADAS.
B - UMA LISTAGEM COM AS PESSOAS MAIS PESADAS.
C - UMA LISTAGEM COM AS PESSOAS MAIS LEVES.
'''

temp = []
princ = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])  # vai criar uma ligação entre o temp e o pric
    temp.clear()  # vai limpar o temp
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, voce cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {maior}Kg.', end='')

for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg.', end='')

for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
