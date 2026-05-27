'''
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
80
CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR CINCO
VALORES NUMERICOS E CADASTRE-OS EM UMA LISTA, JA NA
POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SIRT()).
NO FINAL, MOSTRE A LISTA ORDENADA NA TELA.
-=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=--=-=-=-=-=-=--=-=-
'''

lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if c == 0 or n > lista[-1]:
        lista.append(n)

    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
                pos += 1

print('_=' * 20)
print(f'os valores digitados foram {lista}')
