n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
op = 0
while op != 5:
    print('''[ 1 ]Somar
    [ 2 ]multiplicar
    [ 3 ]Maior
    [ 4 ]Novos numeros
    [ 5 ]sair do programa''')
    op = int(input('Qual é a sua opção: '))
    if op == 1:
        soma = n1 + n2
        print(' A soma de igua a {} '.format (soma))
    elif op == 2:
        prod = n1 * n2
        print(' A soma de igua a {} '.format (prod))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(' A soma de igua a {} '.format (maior))
    elif op == 4:
        print('Informe os numeros novamente!')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('opção invalida! Tente novamente')
    print('-=-' * 10)
print('Fim do programa!')


print('Fim do programa! Volte sempre.')



