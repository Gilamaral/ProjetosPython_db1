print ('--------------------------------------------')
print('Seja bem vindo(a) a Tabuada infinta')
print ('--------------------------------------------')

while True:
    numero = int(input('digite um numero!'))
    print('-' * 20)
    for c in range(0,11):
        print(numero, ' x ', c , ' = ',c*numero)
    print('-' * 20)
    sair = str(input('vc ja terminou s ou n '))
    if sair == 's':
        break