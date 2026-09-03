''' EXERCICIO 89
CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VARIOS
ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA. NO FINAL,
MOSTRE UM BOLETIM CONTENDO A MEDIA DE CADA UM E PERMITA
QUE  OS USUARIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO
INDIVIDUALMENTE.
'''

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append( [ nome, [nota1, nota2], media ] )
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta in 'Nn':
        break

print('-='*30)
print(f'{"Noº":<4} {"Nome":<10} {"Média":>8}')
print('-'*30)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4} {aluno[0]:<10} {aluno[2]:>8.1f}')

while True:
    print('-'*30)
    opcao = int(input('Mostrar a nota de qual aluno? (888 interrompe)'))
    if opcao == 888:
        print('Finalizando...')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} e {ficha[opcao][1]}')
        