import math
num = int(input('digite um numero '))
raiz = math.sqrt(num)
print('a raiz de {} e igual a {}'.format(num, math.ceil(raiz)), end='')
print(' e igual a {:.2f}'.format(raiz))
