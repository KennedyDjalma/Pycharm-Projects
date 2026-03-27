class cores:
    preto = '\033[0;30m'
    vermelho = '\033[0;31m'
    verde = '\033[0;32m'
    amarelo = '\033[0;33m'
    azul = '\033[0;34m'
    roxo = '033[0;35m'
    ciano = '\033[0;36m'
    branco = '\033[0;37m'
    reset = '\033[0m'


nome = input('Digite seu nome: ')
print(cores.vermelho + 'Olá senhor, {}!'.format(nome))
