nome = str(input('Qual é eu nome?'))
if nome == 'Gilvan':
    print('que nome lindo!')
elif nome == 'joao' or nome == 'maria' or nome == 'jose':
    print('Seu nome é bem comum no brasil.')
elif nome in 'ana claudia juliana':
    print('belo nome feminino')
else:
    print('seu nome é bem normal!')
print('bom dia, {}!'.format(nome))