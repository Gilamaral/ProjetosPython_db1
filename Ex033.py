a = int(input('Digite um valor? '))
b = int(input('Digite um valor? '))
c = int(input('Digite um valor? '))
menor =  a
maior = a
#Verificando menor numero
if b < a and b < c:
    menor = b
if c < a and c < c:
    menor = c
#Verificando Maior numero
if b > a and b > c:
    maior = b
if c > a and c > c:
    maior = c
print('o menor numero é {}, e o maior numero é {}'.format(menor, maior))