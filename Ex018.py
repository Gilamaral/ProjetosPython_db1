import math
angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('o angulo de {:.2f} tem o seno de {:.2f}'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('o angulo de {:.2f} tem o cosseno de {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('o angulo de {:.2f} tem o Tangente de {:.2f}'.format(angulo,tangente))