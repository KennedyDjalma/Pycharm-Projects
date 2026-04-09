'''
CRIE UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE
QUATRO PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:
- MÉDIA DO GRUPO.
-QUAL É O HOMEM MAIS VELHO.
-QUANTAS MULHERES T~EM MENOS DE 20 ANOS.
'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for pessoa in range(1, 5):
    print('-_*5 {}ª Pessoa -_*5'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
   # if pessoa == 1 and sexo in 'Mm':
   #     maioridadehomem = idade
    if sexo in 'Mm':
        if maioridadehomem == 0 or idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos.'.format(mediaidade))
print('O Homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
