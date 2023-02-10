n1 = int(input('digite um numero? '))
n2 = int(input('Digite um numero? '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, a multiplicação é {} e a divisão é {:.2f}'. format(s, m, d), end=' ')
print(' A divisão inteira é  {}, a potencia é {}'.format(di,e))

print('a soma é {},\n a multiplicação é {} \n e a divisão é {:.2f} \n'. format(s, m, d), end=' ')
print(' A divisão inteira é  {}, a potencia é {}'.format(di,e))