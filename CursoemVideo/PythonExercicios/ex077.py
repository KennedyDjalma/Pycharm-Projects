'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
77
CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VARIAS PALAVRAS
(NÃO USAR ACENTOS).
DEPOIS DISSO, VOCE DEVE MOSTRAR PARA CADA PALAVRA, QUAIS
SAO SUAS VOGAIS.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

palavras = (
    'aprender', 'programar', 'linguagem', 'python',
    'cursinho', 'gratis', 'estudar', 'praticar',
    'trabalhar', 'mercado', 'programador', 'futuro',
)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
