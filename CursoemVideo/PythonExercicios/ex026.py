'''
FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
- QUANTAS VEZES APARECE A LETRA "A".
- EM QUE POSIÇAO ELA APARECE A PRIMEIRA VEZ.
- EM QUE POSIÇAO ELA APARECE A ULTIMA VEZ.

'''
nome = str(input('Digite uma frase: ')).strip().upper()
print('A frase escrita tem {} caracteres.'.format(len(nome)))
print('A letra "A" aparece {} vezes na frase.'.format(nome.count('A')))
print('A  primeira letra "A" aparece na posição {}.'.format(nome.find('A')))
print('A ultima letra "A" aparece na ultima vez na posição {}.'.format(nome.rfind('A')))
