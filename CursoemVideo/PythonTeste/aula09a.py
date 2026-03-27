frase = 'Aulas de python'
dividido = frase.split()
print('-=' * 30)

print(len(frase)) #comprimento em caracteres
print('-=' * 30)

print(frase.count('a')) #quantidade de letras informadas
print('-=' * 30)

print(frase.upper()) #letras maiusculas
print('-=' * 30)

print(frase[0:15:2])
print('\033[4;30;43m-=\033[m' * 30)

print(frase.replace('python', 'Android')) #muda a palavra
print('-=' * 30)

print(frase.split()) #separa a frase
print(dividido[1]) #consegue escolher qual palavra dividida mostrar
print('-=' * 30)
