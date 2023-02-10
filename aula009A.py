n1 = float(input('digite sua nota do 1º semestre: '))
n2 = float(input('digite sua nota do 2º semestre: '))
m = (n1+n2)/2
print('A sua media do ano foi {:.1f}'.format(m))
if m>= 7.0:
    print('Sua media está boa, Parabens!')
else:
    print('sua media está baixa, precisa estudar mais!')