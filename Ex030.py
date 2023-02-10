numero = int(input('Digite qualquer numero: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} que voce digitou é um numero "PAR"! '.format(numero))
else:
    print('O numero {} que voce digitou é um numero "IMPAR"! '.format(numero))