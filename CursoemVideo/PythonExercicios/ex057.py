'''
    -------------------------------------------------
    57-
    FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA,
    MAS SO ACEITE OS VALORES 'M' OU 'F'.
    CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE
    ATÉ TER UM VALOR CORRETO.
    -------------------------------------------------

'''

'''
r = 'f'
while r != 'F' and r != 'M':
    r = str(input('Digite seu Sexo [M / F]: ')).strip().upper()[0]
    if r == 'M':
        print('Sexo Masculino')
        break
    elif r == 'F':
        print('Sexo Feminino')
        break
    else:
        print('Sexo Invalido')
'''

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


