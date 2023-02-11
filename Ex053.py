
frase = str(input('digite uma frase: ')).strip().upper()
palavras =  frase.split()
junto =''.join(palavras)
print(junto)
inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print(junto, inverso)'''
if inverso == junto:
    print('temos um palindromo {} é {}'.format(junto, inverso))
else:
    print('Não temos um palindromo')




