nome = str(input('Seu nome: ')).strip().lower()
if nome == 'kennedy' or 'jaiane':
    print('\033[2;34m Que nome Lindo! \033[0m')

elif nome == 'djalma' or nome == 'de' or nome == 'santana':
    print('Seu nome é bem popular')

elif nome in ['maria' , 'margarete']:
    print('Nome feminino')

else:
    print('Seu nome é comum')

print('Bom dia, {}'.format(nome))


