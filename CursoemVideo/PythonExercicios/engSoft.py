# for
'''
for item in range(2, 9, 3):  # 2= valor inicial; 9= valor final; 3= passo
    print(item)
'''
from cProfile import label

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
'''
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
#CRIANDO JANELA NO PYTHON
from tkinter import *
janelaPrincipal = Tk()
janelaPrincipal.mainloop()
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
'''
'''
#CRIANDO JANELA NO PYTHON
from tkinter import *
janelaPrincipal = Tk()
texto=Label(master=janelaPrincipal,text='Minha Janela Exibida')
texto.place(x=50,y=100)
janelaPrincipal.mainloop()
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
'''

'''
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
# BOTÃO E JANELA FEITO NO PYTHON
from tkinter import *

def funcClicar():
    print('Botão clicado') #APARECE NO CONSOLE

janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text='Minha Janela Exibida')
texto.pack()

botao = Button(master=janelaPrincipal, text='CLIQUE', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
'''

'''
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
# CRIE UM PROGRAMA COM INTERFACE GRÁFICA EM PYTHON
# QUE RECEBA DOIS NUMEROS E REALIZE A SOMA DE AMBOS.

import tkinter as tk
from tkinter import messagebox

def somar_numeros():
    numero1 = float(entry_numero1.get())
    numero2 = float(entry_numero2.get())
    resultado = numero1 + numero2
    messagebox.showinfo('resultado', f'A soma dos numeros é: {resultado}')

# CRIANDO A JANELA
janela = tk.Tk()
janela.title('Calculadora de soma')

# CRIANDO OS WIDGETS
label_numero1 = tk.Label(janela, text='Numero 1:')
label_numero1.grid(row=0, column=0, padx=10, pady=5, sticky='e')

entry_numero1 = tk.Entry(janela)
entry_numero1.grid(row=0, column=1, padx=10, pady=5)

label_numero2 = tk.Label(janela, text='Numero 2:')
label_numero2.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_numero2 = tk.Entry(janela)
entry_numero2.grid(row=1, column=1, padx=10, pady=5)

botao_somar = tk.Button(janela, text='Somar', command=somar_numeros)
botao_somar.grid(row=2, columnspan=2, padx=10, pady=5)

# RODANDO O LOOP PRINCIPAL
janela.mainloop()
'''
'''
# Utilizando o PyCharm, crie um programa com interface gráfica em Python que
# receba dois números, compare-os e informe se o primeiro é maior, menor ou igual ao segundo.

import tkinter as tk
from tkinter import messagebox


def comp_numeros():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if num1 > num2:
        messagebox.showinfo("Resultado", f"O numero {num1} é maior que {num2}")
    elif num1 == num2:
        messagebox.showinfo("Resultado", f"O numero {num1} é  igual a {num2}")
    else:
        messagebox.showinfo("Resultado", f"O numero {num1} é menor que {num2}")

# Criando a janela
janela = tk.Tk()
janela.title("Comparando Numeros")

# Criando os widgets
label_num1 = tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_comp = tk.Button(janela, text="Comparar", command=comp_numeros)
botao_comp.grid(row=2, columnspan=2, padx=10, pady=5)

# Rodando o loop principal
janela.mainloop()
'''
'''
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
                        #Tratamento de exceções na prática
import tkinter as tk
from tkinter import messagebox


def div_numeros():
    try:
        numero1 = float(entry_numero1.get())
        numero2 = float(entry_numero2.get())
        resultado = numero1 / numero2
        messagebox.showinfo('resultado', f'o quofeciente é {resultado}')
    except ValueError:
        messagebox.showerror('error', 'Insira os numeros validos.')

        # CRIANDO JANELA
janela = tk.Tk()
janela.title("Dividir numeros")

    # CRIANDO OS WIDGETS
label_numero1 = tk.Label(janela, text="Numero 1:")
label_numero1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_numero1 = tk.Entry(janela)
entry_numero1.grid(row=0, column=1, padx=10, pady=5)

label_numero2 = tk.Label(janela, text="Numero 2:")
label_numero2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_numero2 = tk.Entry(janela)
entry_numero2.grid(row=1, column=1, padx=10, pady=5)

botao_div = tk.Button(janela, text="Dividir", command=div_numeros)
botao_div.grid(row=2, columnspan=2, padx=10, pady=5)

    # RODANDO O LOOP PRINCIPAL
janela.mainloop()
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
'''

'''
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
        #Tratamento de eveTratamento de eventos na práticantos na prática
import tkinter as tk

def atualizar_coordenadas(event):
    x = event.x
    y = event.y
    label_coordenadas["text"] = f'coordenadas: X={x}, Y={y}'

# CRIANDO JANELA
janela = tk.Tk()
janela.title("atualizar coordenadas")

#CRIANDO WIDGET
label_coordenadas = tk.Label(janela, text="coordenadas:")
label_coordenadas.pack(padx=200, pady=100)

# LIGANDO O EVENTO DE MOVIMENTO DE MOUSE
janela.bind("<Motion>", atualizar_coordenadas)

# RODANDO O LOOP
janela.mainloop()
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
'''
'''
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
import tkinter as tk
def capturarClic(event):
    x = event.x
    y = event.y
    label_coordenadas["text"] = f'Ultimo click: X={x}, Y={y}'

# CRIANDO A JANELA
janela = tk.Tk()
janela.title("capturar clicks ESQUERDO")

# CRIANDO WIDGETS
label_coordenadas = tk.Label(janela, text="CLIQUE em qualquer lugar da janela")
label_coordenadas.pack(padx=200, pady=100)

# LIGANDO O EVENTO DE CLIQUE DO MOUSE A FUNÇÃO
janela.bind("<Button-1>", capturarClic)

# RODANDO O LOOP
janela.mainloop()
# =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=- # =-=-=-=-=-=-=-=-=--=-=-=-
'''
'''
#CONSTRUTORES E METODO INIT E SELF
#SELF É A FORMA DA CLASSE REFERINDO A ELA MESMA
# __INIT__ É O METODO CONSTRUTOR QUE CRIA OBJETO DA CLASSE

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
'''


class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo


def main():
    c1 = Conta(numero=1, cpf=1, nomeTitular="Kenedy", saldo=1000)
    print(f'Nome do titular {c1.nomeTitular}')
    print(f'Saldo do titular {c1.saldo}')
    print(f'Cpf {c1.cpf}')
    print(f'saldo {c1.saldo}')


if __name__ == '__main__':
    main()
