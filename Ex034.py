salario = float(input('Digite o seu salário atual: R$'))
aum1 = salario * 15/100
aum2 = salario * 10/100

if salario < 1250:
    nsalario = salario + aum1
else:
    nsalario = salario + aum2
aumf = nsalario - salario

print('Seu aumento será de {:.2f} novo salario sera R${:.2f} '.format(aumf,nsalario))