''' EXEMPLO 1
for c in range(0,10, 2):
    print(c)
print('FIM')
'''

''' EXEMPLO 2
i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))

for c in range(i, f+1, p):
    print(c)
'''

''' EXEMPLO 3
n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
'''

s = 0 #EXEMPLO 4
for c in range(0 , 4):
    n = int(input('digite um valor: '))
    s += n
print('a soma dos valores for {}'.format(s))
