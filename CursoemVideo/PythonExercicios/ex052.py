'''
FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA
SE ELE É OU NÃO UM NÚMERO PRIMO.
'''

num = int(input('Digite um número: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[1;34m{c}', end=' ')
        total += 1
    else:
        print(f'\033[1;31m', end=' ')
    print('O número {} foi dividido {} vezes '.format(num, total))
if total == 2:
    print('Por isso ele é primo.')
else:
    print('Por isso NÃO É PRIMO')