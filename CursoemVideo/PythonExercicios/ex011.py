# FAÇA UM PROGRAMA QUE LEIA  A LARGURA E A ALTURA DE UMA
# PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE
# TINTA NECESSARIA PARA PINTA-LA SABENDO QUE CADA LITRO
# DE TINTA ONTA UMA AREA DE 2M² .

larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
print('Sua parede tem dimensão de {} X {} e sua area é de {}'.format(larg, alt, area))
tinta = area / 2
print ('Voce precisa de {}L de tinta'.format(tinta))