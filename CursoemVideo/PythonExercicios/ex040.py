'''
FAÇA UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE
SUMA MEDIA MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A
MEDIA ATINGIDA:
- MEDIA ABAIXO DE 5.0: REPROVADO
- MEDIA ENTRE 5.0 E 6.9: RECUMPERAÇÃO
- MEDIA 7.0 OU SUPERIOR: APROVADO
'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media <= 5:
    print('MEDIA ABAIXO DE 5.0: REPROVADO')
elif media <=  6.9:
    print('MEDIA ENTRE 5.0 E 6.9: RECUMPERAÇÃO')
elif media >= 7.0:
    print('MEDIA APROVADO')
