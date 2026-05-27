'''
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
78
FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMERICOS E GUARDE-OS
EM UMA LISTA.
NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO
E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
'''
listanum = []

maior = 0
menor = 0

for c in range(0, 5):
    listanum.append(int(input(f'digite um valor para a posição {c}:')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print('-=' * 30)
print(' voce digitou os valores {}'.format(listanum))
print(f'o maior valor digitado foi {maior} nas posições ', end='')

for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()

print(f'o menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()
