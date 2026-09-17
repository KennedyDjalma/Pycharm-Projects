'''
EX094
CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VARIAS
PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONARIO
E TODOS OS DICIONARIOS EM UMA LISTA. NO FINAL, MOSTRE:
A - QUANTAS PESSOAS FORAM CADASTRADAS.
B - A MEDIA DE IDADE DO GRUPO.
C - UMA LISTA COM TODAS AS MULHERES.
D - UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MEDIA.
'''

pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo:[M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MmFf':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'NnSs':
            break
        print('ErRo! Responda apenas S ou N.')
        if resposta == 'Ss':
            break
    print('-=' * 30)
    print(f'A- Ao todo temos {len(galera)} pessoas cadastradas.')
    media = soma / len(galera)
    print(f'B- A média de idade é de {media} anos.')
    print('C- As mulheres cadastradas foram: ', end='')
    for p in galera:
        if p['sexo'] in 'Ff':
            print(f'{p["nome"]}', end=' ')
    print()
    print('D- lista de pessoas acima da média: ')
    for p in galera:
        if p['idade'] >= media:
            print('     ')
            for k, v in p.items():
                print(f'{k} = {v}; ', end='')
    print('')
    print('ENCERRADO')
    