'''pessoas = [['Pedro', 25], ['Maria', 19], ['joão', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])'''

''' EXEMPLO 1
teste = list()
teste.append('Kennedy')
teste.append(30)

galera = list()
galera.append(teste[:])

teste[0] = 'Djalminha'
teste[1] = 19
galera.append(teste[:])

print(galera)
'''

''' EXEMPLO 2
galera = [['joao', 34], ['ana', 22], ['bia', 25], ['rita', 28]]
print(galera [3])
'''

''' EXEMPLO 3
galera = [['joao', 34], ['ana', 22], ['bia', 25], ['rita', 28]]
for pessoa in galera:
    print(pessoa[0])
'''

''' EXEMPLO 4
galera = [['joao', 34], ['ana', 22], ['bia', 25], ['rita', 28]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]}  de idade.')
'''

galera = list()
dado = list()
for contador in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
    else:
        print(f'{pessoa[0]} é menor de idade.')