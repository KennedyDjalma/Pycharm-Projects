'''
REFAÇA O DESAFIO 035 DOS  TRIANGULOS, ACRESCENTANDO O RECURSO
DE MOSTRAR QUE TIPO DE TRIANGULO SERÁ FORMADO:
- EQUILATERO = TODOS OS LADOS IGUAIS
- ISÓSCELES = DOIS LADOS IGUAIS
- ESCALENO = TODOS OS LADOS DIFERENTES
'''

r1 = float(input('\033[1;34m Primeiro segmento: '))
r2 = float(input('\033[1;34m Segundo segmento: '))
r3 = float(input('\033[1;34m Terceiro segmento: \033[0m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[0;35m Os segmentos acima PODEM FORMAR um TRIANGULO \033[0m')
    if r1 == r2 == r3:
        print('\033[1;36m EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('\033[0;31m ESCALENO')
    else:
        print('\033[0:32m ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIANGULO')
