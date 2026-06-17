# for
'''
for item in range(2, 9, 3):  # 2= valor inicial; 9= valor final; 3= passo
    print(item)
'''

'''nome = input('Digite seu nome: ')
for letra in nome:
    print(letra)
'''

'''
nomes = ['laura', 'lis', 'guilherme', 'enzo', 'artur']
for nome in nomes:
    print(nome)
'''

'''
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    quadrado = numero ** 2
    print(f'O quadrado de {numero} e {quadrado}')
'''

'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
for numero in numeros:
    soma += numero
print(f'A soma de todos os numeros é {soma}')
'''

'''
texto = 'programação'
letra_para_contar = 'r'
contador = 0

for letra in texto:
    if letra == letra_para_contar:
        contador += 1
print(f'A letra "{letra_para_contar}" apareceu {contador} vezes na palavra "{texto}"')
'''

# WHILE
'''
print('ANTES DO WHILE')
palavra=input('Digite uma palavra: ')
while palavra != 'sair':
    print('PALAVRA DENTRO DE WHILE')
    palavra = input('Digite sair para sair: ')
print('FIM DO laço')
'''

'''while True:
    print('Loop')
    break
'''
'''
# ESTRUTURA DE REPETICAO E CONDICAO
for num in range(1000, 10000):
    menor = num % 100  # obtem o numero dos algarismos menos significativos
    maior = num // 100  # obtem o numero dos algarismos mais significativos
    raiz = menor + maior  # obtem a raiz

    if (raiz * raiz == num):
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('TERMINOU')
print('Saiu',num)
'''
'''
# ESTRUTURA DE REPETICAO E CONDICAO
for num in range(32, 100):
    menor = num % 100  # obtem o numero dos algarismos menos significativos
    maior = num // 100  # obtem o numero dos algarismos mais significativos
    raiz = menor + maior  # obtem a raiz

    if (raiz * raiz == num):  # valida se a raiz gera o numero testado
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('TERMINOU')
print('Saiu', num)
'''
'''
start = int(1000 ** 0.5)  # Aproximação da raiz quadrada de 1000

if start * start < 1000:
    start += 1  # Ajusta para garantir que o quadrado seja pelo menos 1000

end = int(9999 ** 0.5)  # Aproximação da raiz quadrada de 9999

for raiz in range(start, end + 1):
    num = raiz * raiz  # calcula o numero gerado pela raiz
    menor = num % 100  # obtem o numero dos algarismos menos significativos
    maior = num // 100  # obtem o numero dos algarismos mais significativos

    if (menor + maior) == raiz:  # valida se a raiz corresponde a soma
        print(num)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu ', raiz)
'''

'''
# Subprogramas
def nova_funcao():
    print('Olá Mundo')
nova_funcao()
'''
'''
escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)
else:
    def func2(x):
        return x + 2
    s = func2(10)
print(s)
'''


'''# Parâmetros, procedimentos e funções
def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia *
    km_rodado) * multiplicador
    return valor
pagamento = taximetro(3.5)
print(pagamento)'''
'''
def funcao1(x):
    x = 10
    print(f'funcao funcao1 - x = {x}')
def funcao2(x):
    x = 20
    print(f'funcao funcao2 - x = {x}')
    return x
vn = 0
print(f'programa principal - vn = {vn}')
vn = funcao1(vn)
print(f'programa principal - vn = {vn}')
vn = funcao2(vn)
print(f'programa principal - vn = {vn}')
'''