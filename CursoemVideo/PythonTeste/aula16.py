'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
'''

'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')
'''

'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
'''

'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(len(lanche))

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(sorted(lanche))
